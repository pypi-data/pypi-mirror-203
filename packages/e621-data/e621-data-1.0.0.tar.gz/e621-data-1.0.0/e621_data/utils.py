from pathlib import Path
from csv import DictReader
from typing import Iterator
from datetime import datetime


def iterate_csv(filepath: str|Path) -> "Iterator[dict]":
    filepath = Path(filepath)

    with filepath.open("r") as f:
        for line in DictReader(f):
            yield line


def parse_date_string(date_string: str) -> datetime:
    format = r"%Y-%m-%d %H:%M:%S.%f"
    return datetime.strptime(date_string, format)
