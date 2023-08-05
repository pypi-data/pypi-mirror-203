from datetime import datetime

import pytest
from newa_downloader import time_span

valid_start = datetime(2007, 1,1)
valid_end = datetime(2009, 1, 1)

invalid_start = datetime(2001, 1, 1)
invalid_end = datetime(2023, 1, 1)


def test_valid_timespan():
    time_span.validate_timespan(valid_start, valid_end)


def test_invalid_timespan():
    with pytest.raises(time_span.StartTimeOutOfRangeError):
        time_span.validate_timespan(invalid_start, valid_end)
    with pytest.raises((time_span.StartTimeOutOfRangeError,
                        time_span.EndTimeOutOfRangeError)):
        time_span.validate_timespan(invalid_start, invalid_end)
    with pytest.raises(time_span.EndTimeOutOfRangeError):
        time_span.validate_timespan(valid_start, invalid_end)
    with pytest.raises(time_span.EndTimeBeforeStartTimeError):
        time_span.validate_timespan(valid_end, valid_start)
