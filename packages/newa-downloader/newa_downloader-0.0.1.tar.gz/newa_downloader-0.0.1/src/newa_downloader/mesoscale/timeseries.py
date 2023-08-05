from pathlib import Path
from typing import List

from newa_downloader.coordinates import Coordinates
from newa_downloader.core import (
    download_url,
    get_url,
    validate_heights,
    validate_variables,
)
from newa_downloader.time_span import TimeSpan

MID_URL = "mesoscale-ts/v1"

HEIGHTS = [50, 75, 100, 150, 200, 250, 500]

VARS_2D = ['LANDMASK', "LU_INDEX", "ELEVATION"]

VARS_TRANSIENT = [
    'ABLAT_CYL', 'ALPHA', 'HFX', 'HGT', 'LH',
    'NEWA_DOMC', 'NEWA_MASK', 'PBLH', 'PRECIP', 'PSFC', 'Q2', 'RHO',
    'RMOL', 'SEAICE', 'SWDDIR', 'SWDDNI', 'T2', 'TSK', 'UST', 'WD10',
    'WS10', 'ZNT']

VARS_3D_TRANSIENT = ["ACCRE_CYL","WS","WD","PD","T","QVAPOR","TKE"]

ALL_VARIABLES = VARS_2D + VARS_TRANSIENT + VARS_3D_TRANSIENT

def make_dicts(variables: List[str],
               coordinates: Coordinates,
               time_span: TimeSpan=None,
               heights: List[int]=None):

    coordinates.validate_inputs()
    validate_variables(variables, ALL_VARIABLES)

    dicts = [{"variable":variables}, coordinates.get_dict()]

    if time_span is None or all(var in VARS_2D for var in variables):
        validate_variables(variables, VARS_2D)
        return dicts

    time_span.validate_inputs()
    dicts.append(time_span.get_dict())

    if heights is None or all(var in VARS_2D + VARS_TRANSIENT for var in variables):
        return dicts

    validate_heights(heights, HEIGHTS)
    dicts.append({"height": heights})
    return dicts

def download(file_path: Path,
             variables: List[str],
             coordinates: Coordinates,
             time_span: TimeSpan=None,
             heights: List[int]=None):
    dicts = make_dicts(variables, coordinates, time_span, heights)
    url = get_url(MID_URL, coordinates.get_end_string(), dicts)
    download_url(url, file_path)

