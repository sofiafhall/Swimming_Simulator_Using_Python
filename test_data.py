import pytest
from data import parse_time

@pytest.mark.parametrize("raw,expected", [
    ("1:02.45", 62.45),
    ("58.31", 58.31),
    ("10:14.07", 614.07),
    ("  53.10 ", 53.10),
    ("NT", None),
    ("DQ", None),
    ("", None),
    (None, None),
    ("garbage", None),
])
def test_parse_time(raw, expected):
    # Verifies req 1 and req 2
    assert parse_time(raw) == expected