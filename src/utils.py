"""
Utils File

This file contains utility functions for text processing.

"""
import re
from typing import List, Optional


def read_string_from_file(file_path: str) -> Optional[str]:
    """
    Read the contents of a text file and return it as a string.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str or None: The string read from the file, or None if an error occurred.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            string = file.read().strip()
        return string
    except IOError:
        print(f"Error: Failed to read the file '{file_path}'.")
        return None


def remove_extra_newlines(string: str) -> str:
    """
    Removes extra newlines from a string.

    Args:
        string (str): The input string.

    Returns:
        str: The string with extra newlines removed.
    """
    return "\n".join(line for line in string.splitlines() if line.strip())


def separate_paragraphs(text: str) -> List[str]:
    """
    Separates a text into paragraphs.

    Args:
        text (str): The input text.

    Returns:
        List[str]: A list of paragraphs from the input text.
    """
    paragraphs = text.split("\n")
    return paragraphs


def get_unique_sentences(text: str) -> List[str]:
    """
    Split the input text into sentences, remove leading empty lines,
    and return a list of unique sentences.

    Args:
        text (str): The input text containing sentences.

    Returns:
        List[str]: A list of unique sentences.

    """
    text = text.lstrip("\n")  # Remove leading empty lines
    sentences = re.split(r"(?<=[.!?])\s+|\n", text)
    unique_sentences = list(set(sentences))
    # unique_sentences = [
    #     sentence for sentence in unique_sentences if sentence.strip() != ""
    # ]
    return unique_sentences
