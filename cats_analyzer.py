"""
This module provides functionality to read and process cat information from a CSV file.
Each row in the CSV file is expected to contain an id, name, and age of a cat.
"""
from pathlib import Path

ID_CSV_INDEX = 0
NAME_CSV_INDEX = 1
AGE_CSV_INDEX = 2


def get_cats_info(path):
    """
    Retrieve cat information from a CSV file.

    Parameters:
    path (str): The path to the CSV file.

    Returns:
    list[dict[str, str]]: A list of dictionaries containing cat information.

    Note:
    The CSV file should have the following columns in order:
    - ID
    - Name
    - Age

    Raises:
    FileNotFoundError: If the file does not exist.
    IndexError: If a row in the CSV does not have enough columns.
    """
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"The file {path} does not exist.")
    return get_cats_info_from_csv(path)


def get_cats_info_from_csv(path):
    """
    Helper function to read cat information from a CSV file.

    Parameters:
    path (Path): The Path object for the CSV file.

    Returns:
    list[dict[str, str]]: A list of dictionaries containing cat information.

    Raises:
    IndexError: If a row in the CSV does not have enough columns.
    """
    cats_info_list = []
    with path.open(mode="r", encoding="UTF-8") as fr:
        for row in fr.readlines():
            cat_info = row.strip().split(",")
            if len(cat_info) < 3:
                raise IndexError(f"Row {row} does not contain enough columns.")
            cats_info_list.append(
                {"id": cat_info[ID_CSV_INDEX],
                 "name": cat_info[NAME_CSV_INDEX],
                 "age": cat_info[AGE_CSV_INDEX]})
    return cats_info_list
