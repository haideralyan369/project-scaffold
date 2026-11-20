# Project Scaffold

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![CI](https://github.com/haideralyan369/project-scaffold/actions/workflows/ci.yml/badge.svg)

A clean, batteries-included starting point for new Python projects — sensible layout, tests, linting, and CI ready to go.

## Project Layout

```text
project-scaffold/
├── .github/
│   ├── workflows/ci.yml        # GitHub Actions: lint + test
│   ├── ISSUE_TEMPLATE/         # Bug report & feature request templates
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/guide.md               # Usage documentation
├── src/
│   ├── main.py                 # Example entry point
│   └── utils.py                # Reusable helpers
├── tests/test_main.py          # Pytest suite
├── pyproject.toml              # Project metadata & tool config
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/haideralyan369/project-scaffold.git
cd project-scaffold

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install development dependencies
pip install pytest ruff

# 4. Run it
python -m src.main
```

## Testing & Linting

```bash
pytest -q        # run the test suite
ruff check .     # lint the codebase
```

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## License

This project is licensed under the [MIT License](LICENSE).
