"""Convert TCX file to CSV file."""

import os
from pathlib import Path

import pandas as pd
from sport_activities_features.tcx_manipulation import TCXFile

# Class for reading TCX files
tcx_file = TCXFile()


# iterate through files and print total distance of activities
def remove_empty_activities(all_files: list) -> None:
    """Remove tcx files that returns missing features."""
    for i in range(len(all_files)):
        activity = tcx_file.read_one_file(all_files[i])
        temp = activity['total_distance'] / 1000
        if temp == 0:
            print(f'Empty activity in file: {all_files[i]}')
            Path.unlink(Path(all_files[i]))


def delete_empty_csv_files(tcx_csv_directory: str) -> None:
    """Delete empty csv files in tcx_csv directory."""
    basically_empty = 110

    for file in os.listdir(tcx_csv_directory):
        temp_file_size = os.path.getsize(tcx_csv_directory + file)

        if temp_file_size <= basically_empty:
            print(f'Empty csv file: {file} in {tcx_csv_directory} directory')
            Path.unlink(Path(tcx_csv_directory, file))


# Function to check if hertrate exists
def check_file_delete_csv_if_columns_are_nan(
        tcx_csv_directory: str,
        filename: str,
        columns: list = None,
        tcx_directory: str = None,
) -> None:
    """Check if nan columns and delete csv.

    Check if columns are nan in dataframe and delete corresponding csv file.
    """
    if columns is None:
        columns = [
            'heartrates',
            'latitude',
            'longitude',
            'altitudes',
            'distances',
            'total_distance',
            'timestamps',
            'heartrates',
            'speeds',
        ]
    tcx_to_csv_df = pd.read_csv(tcx_csv_directory + filename, sep=';')

    if tcx_to_csv_df[columns].isna().to_numpy().any():
        print(f'Something is empty in {tcx_csv_directory}{filename}')
        Path.unlink(Path(tcx_csv_directory, filename))
        if tcx_directory is not None:
            print('aaaaaaaa')
            Path.unlink(Path(tcx_directory, filename.replace('.csv', '.tcx')))

    # TODO for example, file 983.csv has only 10 empty values in heartrates
    # but only 10 missing values in heartrates out of a few 100 lines
    # should be enough to calculate mean, median, etc.
    # so maybe we could keep this file and just fill the empty values


# Function to compare tcx and csv files if both exist
def delete_unmatching_tcx_csv(
        tcx_directory: str,
        tcx_csv_directory: str,
) -> None:
    """Delete tcx files that are not in csv and vice versa."""
    # Get all files in tcx directory
    tcx_files_in_directory = os.listdir(Path(Path.cwd(), 'tcx'))
    # Get all files in tcx_csv directory
    csv_files_in_directory = os.listdir(Path(Path.cwd(), 'tcx_csv'))
    # Remove .tcx and .csv from filenames
    tcx_files_in_directory = [
        i.replace('.tcx', '') for i in tcx_files_in_directory
    ]
    csv_files_in_directory = [
        i.replace('.csv', '') for i in csv_files_in_directory
    ]
    # Get difference between tcx and csv files
    set_tcx_not_in_csv = set(tcx_files_in_directory) - set(
        csv_files_in_directory,
    )
    set_csv_not_in_tcx = set(csv_files_in_directory) - set(
        tcx_files_in_directory,
    )

    # Delete tcx files that are not in csv
    # i.e. 35.tcx is to be deleted, 35.csv does not exist
    for value in set_tcx_not_in_csv:
        print('Deleting ' + tcx_directory + value + '.tcx')
        Path.unlink(Path(tcx_directory + value + '.tcx'))

    # Delete csv files that are not in tcx
    for value in set_csv_not_in_tcx:
        print('Deleting ' + tcx_csv_directory + value + '.csv')
        Path.unlink(Path(tcx_csv_directory + value + '.csv'))
