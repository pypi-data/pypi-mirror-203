from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import requests

BASE_URL = "https://wps.neweuropeanwindatlas.eu/api"
SUCCESS_CODE = 200

class HeightError(ValueError):
    def __init__(self, height: int, available_heights: List[int]):
        msg = f"Height {height} not one of {available_heights}"
        super().__init__(msg)

class VariableError(ValueError):
    def __init__(self, variable: str, available_variables: List[str]):
        msg = f"Height {variable} not one of {available_variables}"
        super().__init__(msg)

def validate_heights(heights: List[int], available_heights: List[int]):
    for height in heights:
        if height not in available_heights:
            raise HeightError(height, available_heights)


def validate_variables(variables: List[str], available_variables: List[str]):
    for variable in variables:
        if variable not in available_variables:
            raise VariableError(variable, available_variables)


def dict_to_string_list(value_dict: Dict[str, Any]):
    string_list = []
    for key, value in value_dict.items():
        if isinstance(value, datetime):
            string_list.append(f"{key}={value.isoformat()}")
        elif isinstance(value, list):
            string_list.extend([f"{key}={val}" for val in value])
        else:
            string_list.append(f"{key}={value}")
    return string_list


def get_url(mid: str, end: str, dicts: List[dict]):
    path =  "/".join((BASE_URL, mid, end))
    full_string_list = []
    for dic in dicts:
        full_string_list.extend(dict_to_string_list(dic))
    parameter = "&".join(full_string_list)
    return  path +"?" + parameter

def download_url(url: str, file_path: Path):
    print("downloading", url)
    read_and_save_response(requests.get(url), file_path)

def read_and_save_response(re: requests.Response, file_path: Path):
    if re.status_code != SUCCESS_CODE:
        exc_msg = f"Download return with status code {re.status_code}. " + \
              re.content.decode()
        raise ValueError(exc_msg)

    print("Download successful")

    with open(file_path, "wb") as f:
        f.write(re.content)
