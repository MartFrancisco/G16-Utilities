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

*This section is under construction. Therefore, I suggest downloading the files and run in JupyterLab. A bried explanation is given bellow on how the code works*

The code (.ipynb format) is divided in two parts. 
1) The first one [input_preparation](ttps://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/input_preparation.ipynb) is to help creating G16 input files (.com) from a XYZ file of the optimized structure. 
2) The second file [output_processing](ttps://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/output_processing.ipynb)is to process G16 output files and generate data points to plot the ghost atom path.

In order run NICS scan and to obtain ZZ values, the molecule needs to be in the XY plane. 
After making sure the molecule is optimized and in the XY plane, use the **input_preparation.ipynb** file. This code will generate a G16 .com file and you can submit for calculation in a high-performance computer. You need to adjust the code to retrieve your XYZ file and save with the desired name. You will be able to edit in JupyterLab.

**input_preparation.ipynb** Gets XYZ structure, builds graphs to represent a molecule and also represent key points on the molecule that may serve as a path for the ghost atoms. It will show middle points in bonded atoms and middle points in the rings. You will be required to select where the ghost atom will follow. For example, passing antracene XYZ will generate the following structue [example numbering](ttps://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/example_numbering.png). You can select a path, for example path 1, where the ghost atoms are going through 2,R3,8,R2,17,R1,24 [path 1](ttps://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/example_path_1.png) or path 2, where the ghost atoms follow 1,R3,8,R2,17,R1,20 [path 2](ttps://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/example_path_2.png)

**output_processing.ipynb** Gets the output file from G16 calculation and obtains NICS(1)ZZ (in ppm). Again, you should adjust the file names to retrieve correctly on JupyterLab. It will generate a TXT file in which the first colum is the distances of the ghost atoms, and the second column is the NICS(1)ZZ values of the respective ghost atom. With the datapoints you are able to plot NICS scan curves. I gave one example here [NICS scan plot](ttps://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/presentation1.tiff)

I ran G16 NMR calculation on path 2 and the example of input, output, and other related files. You can check in the [NICS scan foldert](ttps://github.com/MartFrancisco/G16-Utilities/tree/main/nics_scan/)

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
