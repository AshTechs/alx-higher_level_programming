#!/usr/bin/python3

def print_square(size):
    """
    Prints a square of '#' characters with the given size length.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if it's a float less than 0.
        ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer or size must be a float")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)

