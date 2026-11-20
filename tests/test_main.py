"""Tests for the scaffold modules."""

from src.main import greet
from src.utils import chunk, slugify


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada! Welcome to your new project."


def test_slugify() -> None:
    assert slugify("Hello, Project Scaffold!") == "hello-project-scaffold"
    assert slugify("  Spaces  ") == "spaces"
    assert slugify("already---slugged") == "already-slugged"


def test_chunk() -> None:
    assert list(chunk(range(5), 2)) == [[0, 1], [2, 3], [4]]
    assert list(chunk([], 3)) == []


def test_chunk_rejects_invalid_size() -> None:
    import pytest

    with pytest.raises(ValueError):
        list(chunk([1, 2], 0))
