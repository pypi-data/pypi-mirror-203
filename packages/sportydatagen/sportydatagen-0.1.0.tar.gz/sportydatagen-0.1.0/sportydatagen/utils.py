"""Utility functions for sportydatagen."""

import csv
from pathlib import Path

from sportydatagen.activity import Activity


# duration,distance,calories,activity_type
def read_basic_dataset(filename: str) -> list:
    """Read basic dataset from a csv file."""
    dataset = []
    with Path.open(Path(filename)) as f:
        reader = csv.reader(f, delimiter=',')
        for activity in reader:
            dataset.append(Activity(activity[4],
                                    activity[1],
                                    activity[2],
                                    activity[3]))
        return dataset

def read_dataset(filename: str) -> list:
    """Read full dataset from a csv file."""
    dataset = []
    with Path.open(filename) as f:
        reader = csv.reader(f,  delimiter=';')
        for activity in reader:
            dataset.append(Activity(activity[1], # is activity_type string
                                    activity[2], # is total_distance float
                                    activity[3], # is total_duration float
                                    activity[4], # is burned calories float
                                    activity[5], # is hr_avg float
                                    activity[6], # is hr_min float
                                    activity[7], # is hr_max float
                                    activity[8], # is altitude_avg float
                                    activity[9], # is altitude_min float
                                    activity[10], # is altitude_max float
                                    activity[11], # is ascent float
                                    activity[12], # is descent float
                                    activity[13], # is speed_max float
                                    activity[14], # is speed_avg float
                                    activity[15])) # is file_name string
        return dataset
