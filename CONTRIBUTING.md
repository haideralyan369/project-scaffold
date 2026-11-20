# Contributing

Thanks for your interest in improving this project!

## Getting Started

1. Fork the repository and clone your fork.
2. Create a branch for your change:

   ```bash
   git checkout -b feature/my-change
   ```

3. Install the development tools:

   ```bash
   pip install pytest ruff
   ```

## Before You Submit

- Run the tests: `pytest -q`
- Run the linter: `ruff check .`
- Keep commits focused and write clear commit messages.
- Update documentation when behavior changes.

## Pull Requests

- Describe **what** changed and **why**.
- Link any related issues.
- Make sure CI passes before requesting review.

## Code Style

- Follow PEP 8 with a line length of 100.
- Add type hints to public functions.
- Write tests for new behavior.
