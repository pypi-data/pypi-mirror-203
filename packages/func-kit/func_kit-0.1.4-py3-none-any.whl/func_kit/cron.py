from croniter import croniter
from datetime import datetime


def generate_times(
    start_time: datetime, end_time: datetime, cron_string: datetime
) -> list[datetime]:
    """Generate a list of times between start_time and end_time
    using the cron_string.

    Args:
        start_time (datetime): The start time.
        end_time (datetime): The end time.
        cron_string (datetime): The cron string.

    Returns:
        list[datetime]: A list of times.

    """
    croniter_obj = croniter(cron_string, start_time)
    times = []
    while True:
        current_time = croniter_obj.get_next(datetime)
        if current_time > end_time:
            break
        times.append(current_time)
    return times
