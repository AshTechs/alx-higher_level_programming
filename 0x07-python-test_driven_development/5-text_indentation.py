#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text based on '.', '?', and ':'
    separators = ['.', '?', ':']
    result = ""
    for char in text:
        result += char
        if char in separators:
            result += '\n\n'

    # Print the processed text
    lines = result.split('\n')
    for line in lines:
        print(line.strip())

