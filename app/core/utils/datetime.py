from datetime import datetime
from zoneinfo import ZoneInfo


def convert_datetime_to_epoch(datetime: datetime) -> int:
    return int(datetime.timestamp())


def convert_epoch_to_datetime(epoch_time: int, time_zone=ZoneInfo('utc')) -> datetime:
    return datetime.fromtimestamp(epoch_time, time_zone)
