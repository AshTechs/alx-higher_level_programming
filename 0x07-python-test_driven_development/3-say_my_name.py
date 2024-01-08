#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints the name based on given first_name and last_name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Defaults to empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    # Print the formatted name
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")

