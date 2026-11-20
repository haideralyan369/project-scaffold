"""Example entry point for the project scaffold."""

from src.utils import slugify


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}! Welcome to your new project."


def main() -> None:
    print(greet("World"))
    print("Slug example:", slugify("Hello, Project Scaffold!"))


if __name__ == "__main__":
    main()
