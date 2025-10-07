# Gaussian 16 Utilities
This repository contains **Python utilities for Gaussian 16**:
You are welcome to contribute to this project!

**Table of content:**
- [Gaussian Input Generator from SMILES](#inp-gen)
- [Intrinsic Reaction Coordinates Figures](#irc-gen)
- [NICS Scan Preparation](#nics-scan)  

<!-- headings -->
<a id="inp-gen"></a>

**Gaussian Input Generator from SMILESr**
   [Check here](https://github.com/MartFrancisco/G16-Utilities/tree/main/input_generator)
   - Reads SMILES strings from Excel/TXT files.  
   - Generates Gaussian input files (`.com`). 

   This script converts molecule data into Gaussian input files.

- **Input format**:  
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

### Default settings
python smiles_to_gaussian.py molecules.xlsx

### Custom settings
python smiles_to_gaussian.py molecules.xlsx \
    --mem 64 --proc 64 \
    --level "wb97xd/6-31+g(d,p)" \
    --charge 1 --mult 2

---

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

<!-- headings -->
<a id="irc-gen"></a>

**Intrinsic Reaction Coordinates Figures**
   [Check here](https://github.com/MartFrancisco/G16-Utilities/tree/main/irc_generator)
   - Parses Gaussian IRC (`.out` / `.log`) files.  
   - Produces **high-quality, publication-ready energy profile plots**.  


Generate publication-quality IRC energy profile plots from Gaussian output file

Features
Parses Gaussian IRC tables and transition state energy
Converts energies to kcal/mol
References energies to the first IRC point
Optional spline smoothing (--smooth)
Customizable fonts (axes, legend/title, ticks)
Saves plots as: .tiff, .jpeg, .jpg
Output filename automatically matches the input file stem

### Basic usage
python irc_plot.py irc_output.out

### With customization
python irc_plot.py irc_s0_f_oqm.out \
    --axis_font "Arial" --axis_font_size 16 \
    --legend_font "Arial" --legend_font_size 16 \
    --tick_font_size 14 \
    --smooth 0.2 \
    --output_format tiff
    
---
---

<!-- headings -->
<a id="nics-scan"></a>

🤝 Contributing

Contributions are welcome!
Feel free to open an issue or submit a pull request with improvements, bug fixes, or new features.
