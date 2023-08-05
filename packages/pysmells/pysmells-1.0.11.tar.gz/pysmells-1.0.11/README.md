# Pysmells

Pysmells is a tool that identifies when something doesn't 'smell right' in a python code, checking for programming errors, inconsistencies and programming style violations. It will then generate a report detailing the results of the analysis. Pysmells is based on the following Python Enhancement Proposals (PEPs): PEP 8, PEP 257 and PEP 20.

## Installation

You can install pysmells using pip:

`pip install pysmells`

Clone this repository:

bash `git clone https://github.com/pysmells/pysmells.git`

## Usage

To use pysmells, navigate to the directory containing the Python files you want to analyze and run the following command:

Arguments:

-p or --project: The project directory containing the subdirectories with Python files to analyze.
-s or --subdirs: The list of subdirectories in the project directory, each representing a software.
-csv or --csv_output: The path and file name for the CSV output report.

`python pysmells.py -p /.../test  -s  Program1 Program2 -csv /.../report.csv`

## Dependencies

pysmells requires the following packages:

- tabulate
- pylint

These dependencies will be automatically installed when you install pysmells using pip.

## License

pysmells is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
