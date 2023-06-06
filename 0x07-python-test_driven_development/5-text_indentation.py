#!/usr/bin/python3
"""
Prints a given text with 2 new lines after each occurrence of '.', '?', ':'.
"""


def text_indentation(text):
    """
    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indented_text = (
        text.replace('.', '.\n\n')
        .replace('?', '?\n\n')
        .replace(':', ':\n\n')
    )

    print(indented_text)
