from pathlib import Path
from typing import List, Tuple

import pytest
from newa_downloader import coordinates
from newa_downloader.mesoscale import climate

valid_c = coordinates.DataPoint(32, 0)
invalid_c = coordinates.DataPoint(-1, 0)

valid_h = [50]
invalid_h = [-1]

valid_3d_v = [("rho", climate.Statistic.Mean)]
valid_2d_v = ["lu_index"]
invalid_3d_v = ["GARBAGE"]

@pytest.mark.parametrize(("static_var, var, coord, height"), [
    ([], valid_3d_v, valid_c, valid_h),
    (valid_2d_v, [], valid_c, None)])
def test_datapoint_download(tmp_path: Path,
                            static_var: List[str],
                            var: List[Tuple[str, climate.Statistic]],
                            coord: coordinates.Coordinates,
                            height: List[int]):
    file = tmp_path/"test_file.nc"
    climate.download(file,static_var, var, coord, height)
