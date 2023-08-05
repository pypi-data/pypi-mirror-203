# E621-Data

Load the e621 export data in a python format lazily.

```python
from e621_data import load_posts

for post in load_posts("./posts-2023-04-14.csv"):
    print(post)
>>>

Post(
    id=491,
    uploader_id=7,
    created_at=datetime.datetime(2007, 2, 17, 10, 35, 32, 756555),
    updated_at=datetime.datetime(2023, 2, 19, 13, 26, 54, 614594),
    source='https://inkbunny.net/Arcturus',
    rating='s',
    tags=[
        '2005',
        '<3',
        'ambiguous_gender',
        'anthro',
        'arcturus_(n)',
        'blue_body',
        'clothed',
        'clothing',
        'crimson',
        'dragon',
        'duo',
        'exclamation_point',
        'eyewear',
        'garrett',
        'gloves',
        'handwear',
        'headphones',
        'inline_skates',
        'jet_set_radio',
        'lizardbeth',
        'male_(lore)',
        'red_body',
        'roller_skates',
        'scalie',
        'simple_background',
        'skating',
        'sunglasses',
        'thief',
        'thief_(series)',
        'upside_down'
    ],
    md5='dee7546d137a6df8bc67ca1c2205836c',
    file_ext='jpg',
    file_size=217339,
    image_width=675,
    image_height=883,
    locked_tags='',
    fav_count=15,
    parent_id=None,
    change_seq=42697063,
    approver_id=17633,
    comment_count=6,
    description='',
    duration=None,
    score=3,
    up_score=7,
    down_score=-4,
    is_deleted=False,
    is_pending=False,
    is_flagged=False,
    is_rating_locked=True,
    is_status_locked=False,
    is_note_locked=False
)
```

## Installation

[https://pypi.org/project/e621-data/](https://pypi.org/project/e621-data/)
```
python -m pip install e621-data
```
