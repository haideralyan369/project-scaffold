# Usage Guide

This guide explains how to use the scaffold as the base for a new project.

## Prerequisites

- Python 3.10 or newer
- Git

## Installation

```bash
git clone https://github.com/haideralyan369/project-scaffold.git
cd project-scaffold
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

## Running the example

```bash
python -m src.main
```

Expected output:

```text
Hello, World! Welcome to your new project.
Slug example: hello-project-scaffold
```

## Using the helpers

```python
from src.utils import chunk, slugify

slugify("My New Post")            # "my-new-post"
list(chunk([1, 2, 3, 4, 5], 2))   # [[1, 2], [3, 4], [5]]
```

## Adapting the scaffold

1. Rename the project in `pyproject.toml`.
2. Replace `src/main.py` with your application entry point.
3. Add tests under `tests/`.
4. Update the README with project-specific details.
