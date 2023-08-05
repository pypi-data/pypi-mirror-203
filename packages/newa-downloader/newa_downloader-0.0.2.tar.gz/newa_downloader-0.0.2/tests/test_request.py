from datetime import datetime
from pathlib import Path

import pytest
from newa_downloader import core


def test_dict_conversion():
    time_string = "2018-12-31T23:30:00"
    test_dict = {
        "num_value": 1,
        "str_value": "test",
        "list": [1],
        "time": datetime.fromisoformat(time_string),
        }
    res = core.dict_to_string_list(test_dict)
    assert res[0] == "num_value=1"
    assert res[1] == "str_value=test"
    assert res[2] == "list=1"
    assert res[3] == "time="+time_string


def test_url():
    url = core.get_url("MID", "END", [{"TEST": "1"}])
    assert url == core.BASE_URL + "/MID/END?TEST=1"


class MockResponse:
    def __init__(self, status_code: int, content: bytes):
        self.status_code = status_code
        self.content = content


def test_download_fail(tmp_path: Path):
    with pytest.raises(ValueError, match="Download return with status code 312. fail"):
        core.read_and_save_response(MockResponse(312, b"fail"), tmp_path) # type: ignore


def test_download_successful(tmp_path: Path):
    file: Path = tmp_path/"result.txt"
    core.read_and_save_response(MockResponse(200, b"success"), file) # type: ignore
    assert file.read_text() == "success"

