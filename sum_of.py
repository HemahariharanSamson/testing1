"""A simple module demonstrating addition."""


def add_numbers(first: int, second: int) -> int:
    """Return the sum of two integers."""
    return first + second


def main() -> None:
    """Run the main program."""
    result = add_numbers(10, 20)
    print(f"Sum: {result}")


if __name__ == "__main__":
    main()
