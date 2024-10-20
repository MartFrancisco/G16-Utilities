# Gaussian 16 Utilities

This repository contains a Python script designed to generate Gaussian input files from SMILES strings. It processes Excel files containing molecule names (in the first column) and SMILES strings (in the second column) to create Gaussian input files.

**Note:** Ensure the Excel file's first row contains the headers "name" and "smiles", as the script filters data based on these keywords.
Check an excel example [here](https://github.com/MartFrancisco/G16-Utilities/blob/main/molecules.xlsx)
Check an input generated by the code [here](https://github.com/MartFrancisco/G16-Utilities/blob/main/Bod.com)

---

## Features

The script allows you to customize memory allocation, number of cores, checkpoint file settings, and theory level. These options can be easily adjusted through flags when running the script.

### Default Settings:
- **Memory:** `32 GB` (modifiable with `--mem`)
- **Cores:** `32` (modifiable with `--proc`)
- **Theory level:** `ωb97xd/def2svp` (modifiable with `--level`)
- **Charge:** `0` (modifiable with `--charge`)
- **Multiplicity:** `1` (modifiable with `--mult`)

---

## Installation

### Clone the Repository

The easiest way to set up these scripts is to clone the repository directly from GitHub. Follow these steps:

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
    mv sml_to_g16.py ~/bin/
    ```

4. Make the script executable:
    ```bash
    chmod u+x ~/bin/sml_to_g16.py
    ```

---

## Usage

### Generating Gaussian Input Files

The script `sml_to_g16.py` reads an Excel file with molecule names and SMILES strings and generates Gaussian input files (.com).

#### Running the Script

1. To run the script with default settings:
    ```bash
    python ~/bin/sml_to_g16.py file_name.xlsx
    ```

2. To modify settings such as memory, cores, theory level, charge, or multiplicity, use flags:
    ```bash
    python ~/bin/sml_to_g16.py file_name.xlsx --mem 64 --proc 64 --level "wb97xd/6-31+g(d,p)" --charge 1 --mult 2
    ```

---

Feel free to customize the script and contribute by submitting pull requests or issues!
