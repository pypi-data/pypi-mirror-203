
from enum import Enum
from pathlib import Path
from typing import List, Tuple

from newa_downloader.coordinates import Coordinates
from newa_downloader.core import (
    download_url,
    get_url,
    validate_heights,
    validate_variables,
)

MID_URL = "mesoscale-atlas/v1"

class Statistic(Enum):
    Mean = "mean"
    Max = "max"
    Min = "min"
    Std = "std"

HEIGHTS = [50, 75, 100, 150, 200, 250, 500]

STATIC_VARIABLES = ['landmask', "lu_index", "elevation"]

SINGLE_LEVEL_VARIABLES = ["WS10", "pbl_height", "T2",
                          "tke50", "rho", "Q2", "Q100", "T100"]

ALL_VARIABLES = [*SINGLE_LEVEL_VARIABLES, "wind_speed", "power_density"]

def make_dicts(static_variables: List[str],
               variable_statistics: List[Tuple[str, Statistic]],
               coordinates: Coordinates,
               heights: List[int]=None):

    var_list = static_variables + [v+"_"+s.value for v, s in variable_statistics]
    var_names = [pair[0] for pair in variable_statistics]

    coordinates.validate_inputs()
    validate_variables(static_variables, STATIC_VARIABLES)

    dicts = [coordinates.get_dict(), {"variable": var_list}]

    validate_variables(var_names, ALL_VARIABLES)


    if heights is None or all(vars in SINGLE_LEVEL_VARIABLES for vars in var_names):
        return dicts

    validate_heights(heights, HEIGHTS)
    dicts.append({"height": heights})
    return dicts


def download(file_path: Path,
             static_variables: List[str],
             variable_statistics: List[Tuple[str, Statistic]],
             coordinates: Coordinates,
             heights: List[int]=None):

    dicts = make_dicts(static_variables, variable_statistics, coordinates, heights)
    url = get_url(MID_URL, coordinates.get_end_string(), dicts)
    download_url(url, file_path)

