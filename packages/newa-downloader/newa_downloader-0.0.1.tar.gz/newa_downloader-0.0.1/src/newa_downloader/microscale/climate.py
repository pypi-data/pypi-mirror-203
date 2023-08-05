from pathlib import Path
from typing import List

from newa_downloader.coordinates import Coordinates
from newa_downloader.core import (
    download_url,
    get_url,
    validate_heights,
    validate_variables,
)

MID_URL = "microscale-atlas/v1"

HEIGHTS = [50, 100, 200]

STATIC_VARIABLES = ["elevation", "rix"]
THREE_D = ["air_dens", "power_dens", "wind_speed", "weib_A_combined", "weib_k_combined"]


def make_dicts(variables: List[str],
               coordinates: Coordinates,
               heights: list[int]=None):
    coordinates.validate_inputs()
    validate_variables(variables, THREE_D + STATIC_VARIABLES)

    dicts = [coordinates.get_dict(), {"variable": variables}]

    if heights is None or all([variables in STATIC_VARIABLES]):
        return dicts

    validate_heights(heights, HEIGHTS)
    dicts.append({"height": heights})
    return dicts


def download(file_path: Path,
             variables: List[str],
             coordinates: Coordinates,
             heights: list[int]=None):
    dicts = make_dicts(variables, coordinates, heights)
    url = get_url(MID_URL, coordinates.get_end_string(), dicts)
    download_url(url, file_path)

