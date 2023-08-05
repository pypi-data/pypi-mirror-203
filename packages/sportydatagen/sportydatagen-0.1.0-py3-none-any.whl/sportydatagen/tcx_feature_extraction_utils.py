"""Manually extracting data from a TCX file."""
import datetime as dt
import os
from pathlib import Path

import pandas as pd
from sport_activities_features import TCXFile


def calculate_duration(read_df_tcx_csv: pd.DataFrame) -> int:
    """Calculate duration of activity in seconds."""
    start_time = dt.datetime.strptime(
        read_df_tcx_csv['timestamps'][0],
        '%Y-%m-%d %H:%M:%S',
    ).astimezone()
    end_time = dt.datetime.strptime(
        read_df_tcx_csv['timestamps'][len(read_df_tcx_csv) - 1],
        '%Y-%m-%d %H:%M:%S',
    ).astimezone()

    return int((end_time - start_time).total_seconds())


def calculate_ascent_descent(read_df_tcx_csv: pd.DataFrame) -> tuple:
    """Calculate ascent and descent of activity in meters."""
    diff = read_df_tcx_csv['altitudes'].diff()

    # Create new columns 'ascent' and 'descent'
    # Calculate ascent
    read_df_tcx_csv['ascent'] = diff.where(diff > 0, 0)
    # Sum of dataframe column ascent
    full_ascent = read_df_tcx_csv['ascent'].sum()

    # Calculate descent
    read_df_tcx_csv['descent'] = (-diff).where(diff < 0, 0)
    # Sum of dataframe column descent
    full_descent = read_df_tcx_csv['descent'].sum()
    return full_ascent, full_descent


def extract_single_tcx_csv_metrics(
    read_df_tcx_csv: pd.DataFrame,
    tcx_directory: str,
    filename: str,
    index: int,
) -> dict:
    """Extract metrics from a single TCX file."""
    # Extract calories using sports_activities_features
    tcx_file = TCXFile()

    current_file = Path(tcx_directory, filename.replace('.csv', '.tcx'))
    # Extract Integral Metrics using sports_activities_features
    activity_metrics = tcx_file.extract_integral_metrics(current_file)
    # Extract calories from dictionary
    calories = activity_metrics['calories']

    # Extract metrics manually from dataframe
    activity_type = read_df_tcx_csv['activity_type'][0]
    total_distance = read_df_tcx_csv['total_distance'][
        len(read_df_tcx_csv) - 1
    ]
    hr_avg = read_df_tcx_csv['heartrates'].mean()
    hr_max = read_df_tcx_csv['heartrates'].max()
    hr_min = read_df_tcx_csv['heartrates'].min()
    altitude_avg = read_df_tcx_csv['altitudes'].mean()
    altitude_max = read_df_tcx_csv['altitudes'].max()
    altitude_min = read_df_tcx_csv['altitudes'].min()
    duration = calculate_duration(read_df_tcx_csv)
    ascent, descent = calculate_ascent_descent(read_df_tcx_csv)
    # speed_min has been removed since it is always 0
    speed_max = read_df_tcx_csv['speeds'].max()
    speed_avg = read_df_tcx_csv['speeds'].mean()

    # Calories are not available in TCX files
    # they are calculated in sport_activities_features
    return {
        'index': index,
        'activity_type': activity_type,
        'total_distance': round(total_distance, 2),
        'duration': duration,
        'calories': calories,
        'hr_avg': round(hr_avg),
        'hr_min': hr_min,
        'hr_max': hr_max,
        'altitude_avg': round(altitude_avg, 2),
        'altitude_min': altitude_min,
        'altitude_max': altitude_max,
        'ascent': ascent,
        'descent': descent,
        'speed_max': speed_max,
        'speed_avg': speed_avg,
        'file_name': filename,
    }


def extract_convert_tcx_to_csv(
    tcx_directory: str = './tcx/',
    tcx_csv_directory: str = './tcx_csv/',
    output_file: str =
    './extracted_metrics/extracted_interval_metrics.csv',
) -> None:
    """Extract data from csv files converted from tcx files using pandas."""
    # Counter for index
    i = 1
    # Create a new dataframe for the extracted metrics
    df_to_save_to = pd.DataFrame()

    for filename in os.listdir(tcx_csv_directory):
        # Print progress
        print(f'Extracting from {filename}')

        # Pandas read csv
        read_df_tcx_csv = pd.read_csv(tcx_csv_directory + filename, sep=';')
        # Extract data from a single TCX file, manually add filename and index
        row_to_append = extract_single_tcx_csv_metrics(
            read_df_tcx_csv,
            tcx_directory,
            filename,
            index=i,
        )

        # Pandas concat dictionary to empty dataframe
        row_to_append = pd.DataFrame([row_to_append]).round(2)
        # Concat rows to dataframe
        df_to_save_to = pd.concat([df_to_save_to, row_to_append])

        # Increment index
        i += 1

    # Save to csv
    df_to_save_to.to_csv(
        Path(output_file),
        sep=';',
        na_rep='NULL',
        index=False,
    )
