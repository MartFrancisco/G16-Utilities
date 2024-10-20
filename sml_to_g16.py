#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
import argparse
import subprocess
import pandas as pd

def smiles_xyz(file_path, mem=32, proc=32, level='opt freq b3lyp/def2svp', charge=0, mult=1):
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Ensure the Excel file has 'name' and 'smiles' columns
        if 'name' not in df.columns or 'smiles' not in df.columns:
            raise ValueError("Excel file must contain 'name' and 'smiles' columns.")

        # Iterate through each row in the DataFrame
        for index, row in df.iterrows():
            name = row['name']
            molecule_data = row['smiles']

            # Run the obabel command for the current molecule
            command = f"obabel -:'{molecule_data}' -oxyz -h --gen3D"

            # Specify the output file path for the .com file
            output_file_path = f"{name}.com"

            # Append the .com extension if not present
            if not output_file_path.lower().endswith(".com"):
                output_file_path += ".com"

            # Write the header lines to the output .com file
            header_lines = [
                f"%chk={name}.chk",
                f"%mem={mem}GB",
                f"%nprocshared={proc}",
                f"# {level}",
                "",
                f"{name}",
                "",
                f"{charge} {mult}"
            ]
            with open(output_file_path, 'w') as output_file:
                output_file.write('\n'.join(header_lines) + '\n')

            # Redirect the obabel command output to the specified file and skip the first two lines
            command += f" | tail -n +3 >> {output_file_path}"

            # Run the modified command
            subprocess.run(command, shell=True)

    except FileNotFoundError:
        print(f"The file at path '{file_path}' was not found.")
    except ValueError as ve:
        print(f"Error in Excel file structure: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert SMILES data to XYZ format and create Gaussian .com files from an Excel file.")
    parser.add_argument("file_path", help="Path to the Excel file containing SMILES data")
    parser.add_argument("--mem", type=int, default=32, help="Amount of memory in GB (default: 32)")
    parser.add_argument("--proc", type=int, default=32, help="Number of processors (default: 32)")
    parser.add_argument("--level", default='opt freq wb97xd/def2svp', help="Calculation level (default: 'opt freq wb97xd/def2svp')")
    parser.add_argument("--charge", type=int, default=0, help="Molecular charge (default: 0)")
    parser.add_argument("--mult", type=int, default=1, help="Multiplicity (default: 1)")

    args = parser.parse_args()

    smiles_xyz(args.file_path, args.mem, args.proc, args.level, args.charge, args.mult)

if __name__ == "__main__":
    main()




