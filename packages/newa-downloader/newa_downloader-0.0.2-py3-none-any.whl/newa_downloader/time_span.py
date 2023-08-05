from dataclasses import dataclass
from datetime import datetime
from typing import Tuple

TIME_RANGE = (datetime.fromisoformat("2005-01-01T00:00:00"),
              datetime.fromisoformat("2018-12-31T23:30:00"))

class EndTimeOutOfRangeError(ValueError):
    def __init__(self, time: datetime):
        msg = f"End time ({time}) outside time range. Last date is {TIME_RANGE[1]}"
        super().__init__(msg)

class StartTimeOutOfRangeError(ValueError):
    def __init__(self, time: datetime):
        msg = f"Start time ({time}) outside time range. First date is {TIME_RANGE[0]}"
        super().__init__(msg)

class EndTimeBeforeStartTimeError(ValueError):
    def __init__(self):
        super().__init__("End time is before start time.")

def validate_timespan(start_time: datetime,
                      end_time: datetime,
                      time_range: Tuple[datetime, datetime]=TIME_RANGE):
    if end_time < start_time:
        raise EndTimeBeforeStartTimeError()
    if not (time_range[0] < end_time < time_range[1]):
        raise EndTimeOutOfRangeError(end_time)
    if not (time_range[0] < start_time < time_range[1]):
        raise StartTimeOutOfRangeError(start_time)


@dataclass
class TimeSpan:
    start_time: datetime
    end_time: datetime

    def get_dict(self):
        return {
            "dt_start": self.start_time,
            "dt_stop": self.end_time,
        }

    def validate_inputs(self):
        validate_timespan(self.start_time, self.end_time)
