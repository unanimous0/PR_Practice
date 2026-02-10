def greeting(name: str = "World") -> str:
    """
    Generate a greeting message.

    Args:
        name: The name to greet (default: "World")

    Returns:
        A greeting message string
    """
    return f"Hello {name}"


if __name__ == "__main__":
    print(greeting())
