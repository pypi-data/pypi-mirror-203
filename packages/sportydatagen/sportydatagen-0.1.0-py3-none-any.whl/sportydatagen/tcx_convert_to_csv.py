"""Convert TCX file to CSV file."""

import os
from pathlib import Path

import pandas as pd
from sport_activities_features.tcx_manipulation import TCXFile

# Class for reading TCX files
tcx_file = TCXFile()


# Function to convert TCX file to CSV file
def read_convert_single_tcx_to_csv(
        input_file: str,
        tcx_csv_directory: str,
) -> None:
    """Read and convert TCX file to CSV file."""
    # Path to input TCX file
    input_file = str(Path(input_file))

    data = tcx_file.read_one_file(
        input_file,
    )  # Represents data as dictionary of lists

    # Convert dictionary of lists to pandas DataFrame
    tcx_to_csv_df = pd.DataFrame.from_dict(data)

    latitude, longitude = True, True

    if latitude & longitude:
        print('Reading file: ' + input_file)
        try:
            # Extract latitude and longitude from positions
            tcx_to_csv_df[['latitude', 'longitude']] = pd.DataFrame(
                tcx_to_csv_df['positions'].tolist(),
            )
            # Drop positions column
            tcx_to_csv_df = tcx_to_csv_df.drop(['positions'], axis=1)
            # Reorder columns
            tcx_to_csv_df = tcx_to_csv_df[
                [
                    'activity_type',
                    'latitude',
                    'longitude',
                    'altitudes',
                    'distances',
                    'total_distance',
                    'timestamps',
                    'heartrates',
                    'speeds',
                ]
            ]

            # Set index name
            tcx_to_csv_df.index.name = 'row_id'

            # Round DataFrame to 2 decimals
            tcx_to_csv_df = tcx_to_csv_df.round(
                {'altitudes': 2, 'distances': 2, 'speeds': 2},
            )

            # Change file extension to .csv
            output_file = Path(tcx_csv_directory +
                               Path(input_file).stem + '.csv')
            print('Converting file: ' + str(output_file))
            # Save DataFrame to CSV file
            tcx_to_csv_df.to_csv(
                output_file,
                index=True,
                header=True,
                sep=';',
            )
        except ValueError:
            print('Error reading file: ' + input_file)
            pass


def read_convert_directory_tcx_files(
        tcx_directory: str,
        tcx_csv_directory: str,
) -> None:
    """Convert TCX file to CSV file."""
    for filename in os.listdir(tcx_directory):
        input_file = Path(tcx_directory, filename)
        read_convert_single_tcx_to_csv(
            input_file=str(input_file),
            tcx_csv_directory=tcx_csv_directory,
        )


# Function to merge CSV files
def merge_csv_files(
        input_files: list,
        output_file: str,
) -> None:
    """Merge CSV files with same columns."""
    # Path to output file
    output_file = str(Path(output_file))

    # List of DataFrames
    dataframes = []

    pd.set_option('display.max_columns', None)

    # Iterate through files
    for input_file in input_files:
        # Read CSV file
        dataframe = pd.read_csv(input_file, sep=';')
        print(dataframe.head())
        # Add extracted feature file name to DataFrame
        dataframe['extracted_csv'] = Path(input_file).name
        # Append DataFrame to list
        dataframes.append(dataframe)

    # Merge all DataFrames
    merged_dataframe = pd.concat(dataframes, axis=0)

    # Delete column index
    del merged_dataframe['index']
    # Create column index
    merged_dataframe['index'] = range(1, len(merged_dataframe) + 1)

    # Shift last column to first position in dataframe
    cols = list(merged_dataframe.columns)
    cols = [cols[-1]] + cols[:-1]
    merged_dataframe = merged_dataframe[cols]

    # Write merged DataFrame to CSV file
    merged_dataframe.to_csv(output_file, index=False, sep=';')
