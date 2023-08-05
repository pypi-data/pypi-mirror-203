from .download import download
from dataclasses import dataclass
from datetime import datetime
from csv import DictReader
from typing import Iterator


@dataclass(frozen=True, slots=True)
class TagAlias:
    id: int
    antecedent_name: str
    consequent_name: str
    created_at: "datetime|None"
    status: str


def load_tag_aliases() -> "Iterator[TagAlias]":
    filepath = download("tag_aliases")
    with filepath.open("r") as f:
        for line in DictReader(f):
            yield TagAlias(
                id=int(line["id"]),
                antecedent_name=line["antecedent_name"],
                consequent_name=line["consequent_name"],
                created_at=datetime.fromisoformat(line["created_at"]) if line["created_at"] else None,
                status=line["status"],
            )
