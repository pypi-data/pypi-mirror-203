"""Convert GPX file to CSV file."""

import os
from pathlib import Path

import pandas as pd
from sport_activities_features.gpx_manipulation import GPXFile


def read_convert_single_gpx_file(input_file: str, output_dir: str) -> None:
    """Read and convert GPX file to CSV file."""
    # Class for reading GPX files
    gpx_file = GPXFile()
    # Read GPX file
    data = gpx_file.read_one_file(
        input_file,
    )  # Represents data as dictionary of lists
    # Path to newly created output CSV file
    output_file = Path(output_dir + Path(input_file).stem + '.csv')
    # Print progress
    print('Converting file: ' + str(output_file))
    # Convert dictionary of lists to pandas DataFrame
    gpx_to_csv_df = pd.DataFrame.from_dict(data)

    latitude, longitude = True, True

    if latitude & longitude:
        try:
            # Extract latitude and longitude from positions
            gpx_to_csv_df[['latitude', 'longitude']] = pd.DataFrame(
                gpx_to_csv_df['positions'].tolist(),
            )
            # Drop positions column
            gpx_to_csv_df = gpx_to_csv_df.drop(['positions'], axis=1)
            # Reorder columns
            gpx_to_csv_df = gpx_to_csv_df[
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
            gpx_to_csv_df.index.name = 'row_id'

            # Round DataFrame to 2 decimals
            gpx_to_csv_df = gpx_to_csv_df.round(
                {'altitudes': 2, 'distances': 2, 'speeds': 2},
            )

            # Save DataFrame to CSV file with semicolon as separator
            gpx_to_csv_df.to_csv(output_file, header=True, sep=';')
        except ValueError:
            print('Error reading file: ' + input_file)
            pass

def read_convert_directory_gpx_files(
    input_dir: str = '../examples/gpx/',
    output_dir: str = '../examples/gpx_csv/',
) -> None:
    """Read and convert all GPX files in directory to CSV files."""
    for filename in os.listdir(input_dir):
        # Path to input GPX file
        input_file = str(Path(input_dir, filename))
        # Path to newly created output CSV file
        read_convert_single_gpx_file(input_file, output_dir)



