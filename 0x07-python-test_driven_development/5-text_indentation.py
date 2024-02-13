#!/usr/bin/python3
"""Prints a text"""


def text_indentation(text):
    """
    Args:
    text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punctuation = ['.', '?', ':']
    lines = []
    current_line = []

    for char in text:
        current_line.append(char)
        if char in punctuation:
            lines.append("".join(current_line).strip())
            current_line = []

    if current_line:
        lines.append("".join(current_line).strip())

    print("\n\n".join(lines), end="")
