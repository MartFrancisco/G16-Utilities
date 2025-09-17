#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3

"""
irc_plot.py

Generate high-quality IRC (Intrinsic Reaction Coordinate) energy profile plots
from Gaussian output files (.out or .log).

Features:
- Parses Gaussian IRC tables and transition state energy
- Converts energies to kcal/mol
- Re-references energies to the first IRC point
- Optional smoothing with spline interpolation
- Customizable fonts and font sizes for axes, legend/title, and ticks
- Saves plots in tiff, jpeg, or jpg formats
- Output filename automatically matches the input file stem

Usage:
    python irc_plot.py irc_s0_f_oqm.out --axis_font "Arial" --axis_font_size 16 \
        --legend_font "Arial" --legend_font_size 16 --tick_font_size 14 \
        --smooth 0.2 --output_format tiff
"""

import re
from pathlib import Path
import numpy as np
import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import argparse

HARTREE_TO_KCAL_MOL = 627.5094

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments with attributes:
            - file: Gaussian .out or .log file
            - axis_font: Font family for axis labels
            - axis_font_size: Font size for axis labels
            - legend_font: Font family for legend/title
            - legend_font_size: Font size for legend/title
            - tick_font_size: Font size for axis ticks
            - smooth: Smoothing factor for spline interpolation
            - units: Energy units ("kcal/mol" or "hartree")
            - output_format: Output file format ("tiff", "jpeg", "jpg")
    """
    parser = argparse.ArgumentParser(description="Generate IRC plot from Gaussian output.")
    parser.add_argument("file", help=".out or .log file from Gaussian")
    parser.add_argument("--axis_font", default="Arial", help="Font family for axis labels")
    parser.add_argument("--axis_font_size", type=int, default=16, help="Font size for axis labels")
    parser.add_argument("--legend_font", default="Arial", help="Font family for legend/title")
    parser.add_argument("--legend_font_size", type=int, default=16, help="Font size for legend/title")
    parser.add_argument("--tick_font_size", type=int, default=14, help="Font size for axis ticks")
    parser.add_argument("--smooth", type=float, default=0, help="Smoothing factor for spline")
    parser.add_argument("--units", choices=["kcal/mol", "hartree"], default="kcal/mol", help="Energy units")
    parser.add_argument("--output_format", choices=["tiff","jpeg","jpg"], default="tiff", help="Output file format")
    return parser.parse_args()

def parse_irc_table(text: str):
    """
    Parse the IRC energy table from a Gaussian output file.

    Args:
        text (str): Full text of Gaussian output file

    Returns:
        tuple:
            - ts_energy (float | None): Energy of the transition state (Hartree)
            - df (polars.DataFrame): DataFrame with columns:
                - "point": IRC point index
                - "rel_energy_hartree": Relative energy (Hartree)
                - "rx_coord": Reaction coordinate
    """
    ts_match = re.search(r"Energies reported relative to the TS energy of\s+([-\d\.Eed+]+)", text)
    ts_energy = float(ts_match.group(1)) if ts_match else None

    block_match = re.search(r"Energy\s+RxCoord\s*\n(.*?)(?:\n\s*\n|\Z)", text, re.DOTALL)
    block = block_match.group(1) if block_match else ""

    rows = []
    for line in block.splitlines():
        m = re.match(r"^\s*(\d+)\s+([-\d\.Ee+]+)\s+([-\d\.Ee+]+)", line)
        if m:
            idx = int(m.group(1))
            rel_e = float(m.group(2))
            rx = float(m.group(3))
            rows.append((idx, rel_e, rx))

    df = pl.DataFrame(rows, schema=["point", "rel_energy_hartree", "rx_coord"], orient="row")
    return ts_energy, df

def process_energies(df: pl.DataFrame, ts_energy: float | None):
    """
    Process IRC energies:
    - Add absolute energy if TS energy is known
    - Convert to kcal/mol
    - Re-reference to local minimum

    Args:
        df (polars.DataFrame): DataFrame with columns ["point", "rel_energy_hartree", "rx_coord"]
        ts_energy (float | None): TS energy in Hartree

    Returns:
        polars.DataFrame: DataFrame with additional columns:
            - "abs_energy_hartree"
            - "rel_energy_kcalmol"
            - "rel_energy_minref_kcalmol"
    """
    if ts_energy is not None:
        df = df.with_columns(
            (pl.lit(ts_energy) + pl.col("rel_energy_hartree")).alias("abs_energy_hartree")
        )
    else:
        df = df.with_columns(pl.lit(None).alias("abs_energy_hartree"))

    df = df.with_columns([
        (pl.col("rel_energy_hartree") * HARTREE_TO_KCAL_MOL).alias("rel_energy_kcalmol")
    ])

    min_energy = df[0, "rel_energy_kcalmol"]
    df = df.with_columns(
        (pl.col("rel_energy_kcalmol") - min_energy).alias("rel_energy_minref_kcalmol")
    )

    return df

def plot_irc(df: pl.DataFrame, filename: str, smooth=0, units="kcal/mol",
             axis_font="Arial", axis_font_size=16, legend_font="Arial", legend_font_size=16,
             tick_font_size=14, figsize=(12,10), output_format="tiff"):
    """
    Plot IRC energy profile.

    Args:
        df (polars.DataFrame): Processed IRC DataFrame
        filename (str): Output filename (stem)
        smooth (float): Spline smoothing factor
        units (str): Energy units ("kcal/mol" or "hartree")
        axis_font (str): Font family for axis labels
        axis_font_size (int): Font size for axis labels
        legend_font (str): Font family for legend/title
        legend_font_size (int): Font size for legend/title
        tick_font_size (int): Font size for axis ticks
        figsize (tuple): Figure size
        output_format (str): File format ("tiff", "jpeg", "jpg")
    """
    x = df["point"].to_numpy()
    if units == "kcal/mol":
        y = df["rel_energy_minref_kcalmol"].to_numpy()
        y_label = r"$\Delta E$ (kcal mol$^{-1}$)"
    else:
        y = df["rel_energy_hartree"].to_numpy()
        y = y - np.min(y)
        y_label = r"$\Delta E$ (Hartree)"

    if smooth > 0:
        xs = np.linspace(x.min(), x.max(), 400)
        spline = UnivariateSpline(x, y, s=smooth)
        ys = spline(xs)
    else:
        xs, ys = x, y

    font_dict = {"family": axis_font, "size": axis_font_size}

    sns.set_theme(style="white")
    fig, ax = plt.subplots(figsize=figsize)

    ax.plot(xs, ys, lw=2, color="black")

    ax.set_xlabel("Reaction Coordinate", fontdict=font_dict, color='black')
    ax.set_ylabel(y_label, fontdict=font_dict, color='black')
    ax.set_title("IRC Energy Profile", fontdict={"family": legend_font, "size": legend_font_size}, color='black')

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)

    ax.tick_params(axis="both", direction="out", length=8, width=3, which="both",
                   labelsize=tick_font_size, colors='black')

    plt.tight_layout()

    output_file = Path(filename).with_suffix(f".{output_format}")
    plt.savefig(output_file, format=output_format, dpi=600)
    print(f"Plot saved as {output_file}")

def main():
    args = parse_args()
    file_path = Path(args.file)
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} does not exist")

    text = file_path.read_text()
    ts_energy, df = parse_irc_table(text)
    df = process_energies(df, ts_energy)
    plot_irc(df, filename=file_path.stem, smooth=args.smooth, units=args.units,
             axis_font=args.axis_font, axis_font_size=args.axis_font_size,
             legend_font=args.legend_font, legend_font_size=args.legend_font_size,
             tick_font_size=args.tick_font_size, output_format=args.output_format)

if __name__ == "__main__":
    main()

