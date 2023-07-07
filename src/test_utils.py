"""
test_utils.py - Test cases for utility functions

This module contains test cases for various utility functions in the `utils` module.
Each test case is implemented as a function and uses the pytest framework for testing.
"""

from .utils import read_string_from_file, remove_extra_newlines, separate_paragraphs


def test_read_string_from_file(tmp_path):
    """
    Test case for read_string_from_file function.

    Parameters:
    - tmp_path: pytest fixture for a temporary directory path.

    Reads a string from a file and asserts that the result matches the expected string.
    """
    file_path = tmp_path / "sample.txt"
    file_path.write_text("This is a test file.")

    result = read_string_from_file(str(file_path))

    assert result == "This is a test file."


def test_read_string_from_file_nonexistent_file(tmp_path):
    """
    Test case for read_string_from_file function with a nonexistent file.

    Parameters:
    - tmp_path: pytest fixture for a temporary directory path.

    Reads a string from a nonexistent file and asserts that the result is None.
    """
    file_path = tmp_path / "nonexistent.txt"

    result = read_string_from_file(str(file_path))

    assert result is None


def test_remove_extra_newlines():
    """
    Test case for remove_extra_newlines function.

    Removes extra newlines from a given input string and asserts
    that the result matches the expected string.
    """
    input_string = "Hello,\n\nThis is a\n\n\n\nsample text.\n\nThank you."

    result = remove_extra_newlines(input_string)

    assert result == "Hello,\nThis is a\nsample text.\nThank you."


def test_separate_paragraphs():
    """
    Test case for separate_paragraphs function.

    Separates paragraphs in a given input string and asserts that the result is
    a list of paragraphs.
    """
    test = "Hello,\n\nThis is a sample text.\n\nThank you."
    result = separate_paragraphs(test)
    print(result)

    assert result == ["Hello,", "", "This is a sample text.", "", "Thank you."]
