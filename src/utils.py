"""Reusable helper functions."""

import re
from typing import Iterable, Iterator, List


def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def chunk(items: Iterable, size: int) -> Iterator[List]:
    """Split an iterable into chunks of at most `size` items."""
    if size < 1:
        raise ValueError("size must be at least 1")

    batch: List = []
    for item in items:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
