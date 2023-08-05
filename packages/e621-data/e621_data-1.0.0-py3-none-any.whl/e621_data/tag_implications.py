from .utils import iterate_csv, parse_date_string
from dataclasses import dataclass
from datetime import datetime
from typing import Iterator
from pathlib import Path


@dataclass(frozen=True, slots=True)
class TagImplication:
    id: int
    antecedent_name: str
    consequent_name: str
    created_at: "datetime|None"
    status: str


def load_tag_implications(filepath: str|Path) -> "Iterator[TagImplication]":
    for line in iterate_csv(filepath):
        yield TagImplication(
            id=int(line["id"]),
            antecedent_name=line["antecedent_name"],
            consequent_name=line["consequent_name"],
            created_at=parse_date_string(line["created_at"]) if line["created_at"] else None,
            status=line["status"],
        )
