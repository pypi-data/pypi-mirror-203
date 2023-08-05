from datetime import date, timedelta
from pathlib import Path
import gzip
import requests

CACHE_DIR = Path(".cache/e621-data")
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def download(name: str) -> Path:
    day = date.today()
    url = generate_url(name, day)
    cache_path = CACHE_DIR / generate_cache_key(name, day)
    if not cache_path.exists():
        remove_old_cache(name)
        r = requests.get(url)
        text = gzip.decompress(r.content).decode()
        cache_path.write_text(text)

    return cache_path


def generate_cache_key(name: str, day: date) -> str:
    return f"{name}-{day.strftime('%Y-%m-%d')}"


def generate_url(name: str, day: date) -> str:
    # Yesterdays date will always have a dump
    yesterdays_date = day - timedelta(days=1)
    date_str = yesterdays_date.strftime('%Y-%m-%d')
    return f"https://e621.net/db_export/{name}-{date_str}.csv.gz"


def remove_old_cache(name: str):
    for path in CACHE_DIR.iterdir():
        if path.name.startswith(f"{name}-"):
            path.unlink()
