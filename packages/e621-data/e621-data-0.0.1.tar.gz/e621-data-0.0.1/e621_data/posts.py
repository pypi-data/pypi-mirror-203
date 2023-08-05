from .download import download
from dataclasses import dataclass
from datetime import datetime
from csv import DictReader
from typing import Iterator


@dataclass(frozen=True, slots=True)
class Post:
    id: int
    uploader_id: int
    created_at: "datetime|None"
    updated_at: "datetime|None"

    source: str
    rating: str
    tags: "list[str]"

    md5: str
    file_ext: str
    file_size: int
    image_width: int
    image_height: int

    locked_tags: str
    fav_count: int
    parent_id: "None|int"
    change_seq: int
    approver_id: "None|int"
    comment_count: int
    description: str
    duration: "float|None"

    score: int
    up_score: int
    down_score: int

    is_deleted: bool
    is_pending: bool
    is_flagged: bool
    is_rating_locked: bool
    is_status_locked: bool
    is_note_locked: bool


def load_posts() -> "Iterator[Post]":
    filepath = download("posts")

    with filepath.open("r") as f:
        for line in DictReader(f):
            yield Post(
                id=int(line["id"]),

                created_at=datetime.fromisoformat(line["created_at"]) if line["created_at"] else None,
                updated_at=datetime.fromisoformat(line["updated_at"]) if line["updated_at"] else None,

                parent_id=int(line["parent_id"]) if line["parent_id"] else None,
                uploader_id=int(line["uploader_id"]),
                approver_id=int(line["approver_id"]) if line["approver_id"] else None,

                rating=str(line["rating"]),
                tags=str(line["tag_string"]).split(" "),

                description=str(line["description"]),
                change_seq=int(line["change_seq"]),
                source=str(line["source"]),
                locked_tags=str(line["locked_tags"]),
                fav_count=int(line["fav_count"]),
                comment_count=int(line["comment_count"]),

                duration=int(line["duration"]) if line["duration"] else None,
                md5=str(line["md5"]),
                file_size=int(line["file_size"]),
                file_ext=str(line["file_ext"]),
                image_width=int(line["image_width"]),
                image_height=int(line["image_height"]),

                score=int(line["score"]),
                up_score=int(line["up_score"]),
                down_score=int(line["down_score"]),

                is_deleted=line["is_deleted"] == "t",
                is_flagged=line["is_flagged"] == "t",
                is_pending=line["is_pending"] == "t",
                is_note_locked=line["is_note_locked"] == "t",
                is_rating_locked=line["is_rating_locked"] == "t",
                is_status_locked=line["is_status_locked"] == "t",
            )
