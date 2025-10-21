# Gaussian 16 Utilities
The repository contains *Python utilities for Gaussian 16*.

**Table of content:**
- [Gaussian Input Generator from SMILES](#inp-gen)
- [Intrinsic Reaction Coordinates Figures](#irc-gen)
- [NICS Scan Preparation](#nics-scan) 
- [Installations](#install) 

---
---

<!-- headings -->
<a id="inp-gen"></a>

## **Gaussian Input Generator from SMILES** [Check here](https://github.com/MartFrancisco/G16-Utilities/tree/main/input_generator)
   - Reads SMILES strings from Excel or txt files.  
   - Generates Gaussian input files (`.com`). 

- **Input format for the code**:  
  - **Excel file** (`.xlsx`) with columns `name` and `smiles` (first row = headers).  
    - Example: [molecules.xlsx](https://github.com/MartFrancisco/G16-Utilities/blob/main/molecules.xlsx)  
  - **Text file** (`.txt`) with `name smiles` (separated by whitespace).  

- **Output**: Gaussian input files (`.com`).  
  - Example: [Bod.com](https://github.com/MartFrancisco/G16-Utilities/blob/main/Bod.com)  

### Features
- Customizable memory, cores, level of theory, charge and multiplicity.  
- Defaults (modifiable via flags):  
  - **Memory:** `32 GB` → `--mem`  
  - **Cores:** `32` → `--proc`  
  - **Level of theory:** `ωB97XD/def2svp` → `--level`  
  - **Charge:** `0` → `--charge`  
  - **Multiplicity:** `1` → `--mult`  

### Usage

#### 1) Default settings
python smiles_to_gaussian.py molecules.xlsx

#### 2) Custom settings
python smiles_to_gaussian.py molecules.xlsx \
    --mem 64 --proc 64 \
    --level "wb97xd/6-31+g(d,p)" \
    --charge 1 --mult 2

---

<!-- headings -->
<a id="irc-gen"></a>

## **Intrinsic Reaction Coordinates Figures** [Check here](https://github.com/MartFrancisco/G16-Utilities/tree/main/irc_generator)
   - Parses Gaussian IRC (`.out` or `.log`) files.  
   - Produces **high-quality, publication-ready energy profile plots**.  

### Features
- Customizable font axis, legend, title, tick marks, image format (.tiff, .jpeg, .jpg).
- Defaults (modifiable via flags): 
  - **Axis font:** `Arial` → `--axis_font`  
  - **Axis font size:** `16` → `--axis_font_size`  
  - **Legend font:** `Arial` → `--legend_font`  
  - **Legend font size:** `16` → `--legend_font_size`  
  - **Tick font size:** `14` → `--tick_font_size`  
  - **Smooth:** `0.0` → `--smooth`  
  - **Figure format:** `.tiff` → `--output_format` 

### Usage

#### 1) Default settings
python irc_plot.py irc_output.out

#### 2) Custom settings
python irc_plot.py irc_s0_f_oqm.out \
    --axis_font "Arial" --axis_font_size 16 \
    --legend_font "Arial" --legend_font_size 16 \
    --tick_font_size 14 \
    --smooth 0.2 \
    --output_format tiff
    
---

<!-- headings -->
<a id="nics-scan"></a>

## **NICS Scan Preparation** [Check here](https://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan)

**This section is under construction.** For now, it is recommended to download the files and run them in **JupyterLab**. A brief explanation of how the code works is given below.

The repository contains two main Jupyter notebooks for performing NICS (Nucleus Independent Chemical Shift) scans using **Gaussian 16 (G16)**:

1. **[input_preparation.ipynb](https://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/input_preparation.ipynb)**  
   Prepares G16 input files (`.com`) from an optimized XYZ structure.

2. **[output_processing.ipynb](https://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/output_processing.ipynb)**  
   Processes G16 output files to generate data points for plotting the ghost atom path.

---

## Workflow Overview

1. Ensure your molecule is optimized and oriented in the **XY plane** (necessary for accurate NICS ZZ calculations).  
2. Run **input_preparation.ipynb** to generate a G16 `.com` input file. Adjust the code to load your XYZ file and save with the desired name.  
3. Submit the `.com` file for calculation on a high-performance computer.  
4. Once the calculation is finished, run **output_processing.ipynb** to extract NICS(1)ZZ values and generate a text file with the results.  

---

## `input_preparation.ipynb`

- Loads an XYZ structure and builds a molecular graph.  
- Identifies **key points** for the ghost atom path:  
  - Midpoints of bonds  
  - Centroids of rings  
- The user selects a path for the ghost atom.  

**Example:**  
For anthracene, the notebook generates the following [numbering scheme](https://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/antracene_d2h/example_numbering.png).  

You can define different paths:  

- **Path 1:** `2, R3, 8, R2, 17, R1, 24` — [example](https://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/antracene_d2h/example_path_1.png)  
- **Path 2:** `1, R3, 8, R2, 17, R1, 20` — [example](https://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/antracene_d2h/example_path_2.png)  

> The generated `.com` file can then be submitted to Gaussian 16.

---

## `output_processing.ipynb`

- Loads the Gaussian 16 output file.  
- Extracts **NICS(1)ZZ values** (ppm) along the selected ghost atom path.  
- Generates a TXT file with:  
  - **Column 1:** Ghost atom distances  
  - **Column 2:** NICS(1)ZZ values  

These data points can be used to plot NICS scan curves.  
Example plot: [NICS scan](https://github.com/MartFrancisco/G16-Utilities/blob/main/nics_scan/Presentation1.tiff)

---

## Examples and Data

- Example input and output files (including paths) are available in the [NICS scan folder](https://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/).  
- The example uses **Path 2** for the ghost atom scan.  

---

## Notes

- You need to edit the notebook paths and filenames according to your system.  
- It is recommended to run the notebooks in **JupyterLab** for easy interaction with input structures and ghost atom paths.  

---

<!-- headings -->
<a id="install"></a>

## Installation

You can either:

- **Download the individual `.py` files** and run them locally, or  
- **Clone the entire repository** from GitHub, as described bellow.  

1. Load Git on the CHPC (Center for High Performance Computing) environment:
    ```bash
    module load git
    ```

2. Clone the repository using:
    ```bash
    git clone git@github.com:MartFrancisco/G16-Utilities.git
    ```

3. Move the Python script to your `~/bin/` directory:
    ```bash
    mv smiles_to_gaussian.py ~/bin/
    ```

4. Make the script executable:
    ```bash
    chmod u+x ~/bin/smiles_to_gaussian.py
    ```

---

### Requirements

Before using the script, ensure you have the following Python packages installed:

- **pandas**: For data manipulation and analysis.
- **openpyxl**: For reading Excel files.
- **Open Babel**: For converting chemical file formats.

You can install the required Python packages using pip:

```bash
pip install pandas openpyxl
```

OpenBabel instalation depends on the operating system:

1) For Ubunto/Debian
```bash
sudo apt-get install openbabel
```
2) For macOS (using Homebrew)
```bash
brew install open-babel
```
3) Windows - You need to dowload directly from OpenBabel website

--- 

🤝 Contributing

Contributions are welcome!
Feel free to open an issue or submit a pull request with improvements, bug fixes, or new features.
