from datetime import datetime
from pathlib import Path
from typing import List, Type

import pytest
from newa_downloader import coordinates, core, time_span
from newa_downloader.mesoscale import timeseries

valid_c = coordinates.DataPoint(32, 0)
invalid_c = coordinates.DataPoint(-1, 0)

valid_t = time_span.TimeSpan( datetime(2007, 1,1,0), datetime(2007,1,1,2))
invalid_t =  time_span.TimeSpan( datetime(2001, 1,1,0), datetime(2007,1,1,2))

valid_h = [50]
invalid_h = [-1]

valid_4d_v = ["TKE"]
valid_3d_v = ["RHO"]
valid_2d_v = ["LU_INDEX"]
invalid_v = ["GARBAGE"]


def test_datapoint_make_dicts():
    dict_list = timeseries.make_dicts(valid_4d_v, valid_c, valid_t, valid_h)
    assert dict_list[0]["variable"] == valid_4d_v
    assert dict_list[1]["latitude"] == valid_c.latitude


@pytest.mark.parametrize(("var, coord, time, height"),[
    (valid_2d_v, valid_c, None, None),
    (valid_3d_v, valid_c, valid_t, None),
    (valid_3d_v, valid_c, valid_t, valid_h),
    (valid_4d_v, valid_c, valid_t, valid_h),
])
def test_valid_datapoint(var: List[str],
                         coord: coordinates.Coordinates,
                         time: time_span.TimeSpan,
                         height: List[int]):
    timeseries.make_dicts(var, coord, time, height)


@pytest.mark.parametrize(("var, coord, time, height, error_type"), [
    (valid_4d_v, valid_c, valid_t, invalid_h, core.HeightError),
    (invalid_v, valid_c, valid_t, valid_h, core.VariableError),
    (valid_4d_v, valid_c, None, None, core.VariableError),
    (valid_4d_v, invalid_c, valid_t, valid_h, coordinates.CoordinateOutOfRangeError),
    (valid_3d_v, valid_c, None, None, core.VariableError),
])
def test_invalid_datapoint(var: List[str],
                           coord: coordinates.Coordinates,
                           time: time_span.TimeSpan,
                           height: List[int], error_type: Type):
    with pytest.raises(error_type):
        timeseries.make_dicts(var, coord, time, height)


def test_datapoint_url():
    dict_list = timeseries.make_dicts(valid_4d_v, valid_c, valid_t, valid_h)
    url = core.get_url("mesoscale-ts/v1", "get-data-point", dict_list)
    assert url == core.BASE_URL + "/mesoscale-ts/v1/get-data-point?" + \
        "variable=TKE&latitude=32&longitude=0&dt_start=2007-01-01T00:00:00&dt_stop=2007-01-01T02:00:00&height=50"

@pytest.mark.parametrize(("var, coord, time, height"),[
    (valid_2d_v, valid_c, None, None),
    (valid_3d_v, valid_c, valid_t, None),
    (valid_3d_v, valid_c, valid_t, valid_h),
    (valid_4d_v, valid_c, valid_t, valid_h),
])
def test_datapoint_download(tmp_path: Path,
                            var: List[str],
                            coord: coordinates.Coordinates,
                            time: time_span.TimeSpan,
                            height: List[int]):
    file = tmp_path/"test_file.nc"
    timeseries.download(file,var, coord, time, height)
