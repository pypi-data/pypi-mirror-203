from .download import download
from dataclasses import dataclass
from csv import DictReader
from typing import Iterator


@dataclass(frozen=True, slots=True)
class Tag:
    id: int
    name: str
    category: str
    post_count: int


def load_tags() -> "Iterator[Tag]":
    filepath = download("tags")
    with filepath.open("r") as f:
        for line in DictReader(f):
            yield Tag(
                id=int(line["id"]),
                name=line["name"],
                category=category_number_to_name(line["category"]),
                post_count=int(line["post_count"]),
            )


def category_number_to_name(category: str) -> str:
    lookup = {
        0: "general",
        1: "artist",
        3: "copyright",
        4: "character",
        5: "species",
        6: "invalid",
        7: "meta",
        8: "lore",
    }
    return lookup[int(category)]
