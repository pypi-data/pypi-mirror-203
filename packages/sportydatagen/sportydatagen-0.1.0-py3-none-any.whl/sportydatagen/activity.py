"""Module containing the Activity class."""


class Activity:

    r"""Class representing an activity.

    Args:
    ----
        activity_type (str): Type of the activity (biking, running, ...)
        total_distance (float): Total distance of the activity in meters.
        duration (float): Duration of the activity in seconds.
        calories (float): Calories burned during the activity.
        hr_avg (float): Average heart rate during the activity.
        hr_min (float): Minimum heart rate during the activity.
        hr_max (float): Maximum heart rate during the activity.
        altitude_avg (float): Average altitude during the activity.
        altitude_min (float): Minimum altitude during the activity.
        altitude_max (float): Maximum altitude during the activity.
        ascent (float): Ascent during the activity.
        descent (float): Descent during the activity.
        speed_max (float): Maximum speed during the activity.
        speed_avg (float): Average speed during the activity.
        file_name (str): Name of the file containing the activity.
    """

    def __init__(self: 'Activity',
                 activity_type: str = None,
                 distance: float = None,
                 duration: float = None,
                 calories: float = None,
                 hr_avg: float = None,
                 hr_min: float = None,
                 hr_max: float = None,
                 altitude_avg: float = None,
                 altitude_min: float = None,
                 altitude_max: float = None,
                 ascent: float = None,
                 descent: float = None,
                 speed_max: float = None,
                 speed_avg: float = None,
                 file_name: float = None) -> None:
        """Initialize the activity."""
        self.activity_type = activity_type
        self.duration = duration
        self.distance = distance
        self.calories = calories
        self.hr_avg = hr_avg
        self.hr_min = hr_min
        self.hr_max = hr_max
        self.altitude_avg = altitude_avg
        self.altitude_min = altitude_min
        self.altitude_max = altitude_max
        self.ascent = ascent
        self.descent = descent
        self.speed_max = speed_max
        self.speed_avg = speed_avg
        self.file_name = file_name

    def __str__(self: 'Activity') -> str:
        """Return the string representation of the activity."""
        return (f'Activity: {self.activity_type}, '
                f'Total duration: {self.duration} seconds, '
                f'Total distance: {self.distance} meters, '
                f'Calories burned: {self.calories}, '
                f'Average hertrate: {self.hr_avg}, '
                f'Minimum heartrate: {self.hr_min}, '
                f'Maximum heartrate: {self.hr_max}, '
                f'Average altitude: {self.altitude_avg}, '
                f'Minimum altitude: {self.altitude_min}, '
                f'Maximum altitude: {self.altitude_max}, '
                f'Ascent: {self.ascent}, '
                f'Descent: {self.descent}, '
                f'Maximum speed: {self.speed_max}, '
                f'Average speed: {self.speed_avg}, '
                f'Original filename: {self.file_name}'
                )
