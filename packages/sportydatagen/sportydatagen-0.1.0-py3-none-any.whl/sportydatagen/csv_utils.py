"""Python script to find and print missing csv files.

Prints missing files from all possible numbered
sequence of tcx files converted to csv files. Csv files are stored in
tcx_csv directory. The script will print a list of missing files.
Files are missing if they have not been correctly converted to csv format.
"""

import os
from pathlib import Path


def create_list_of_all_possible_files(number_of_files: int) -> list:
    """Create a list of all possible files."""
    all_possible_csv_files = []
    for i in range(1, number_of_files + 1):
        all_possible_csv_files.append(f'{i}.csv')
    return all_possible_csv_files


def missing_csv_files(directory_path: str, number_of_files: int) -> list:
    """Find and print missing files.

    Args:
    ----
    directory_path (str): Path to directory with csv files.
    number_of_files (int): Number of files.

    Returns:
    -------
    str: List of missing files.
    """
    csv_files_in_directory = os.listdir(Path(directory_path))

    all_possible_files = create_list_of_all_possible_files(number_of_files)

    set_of_actual_csv_files = set(csv_files_in_directory)
    set_of_possible_csv_files = set(all_possible_files)

    return sorted(
        set_of_possible_csv_files - set_of_actual_csv_files,
    )
