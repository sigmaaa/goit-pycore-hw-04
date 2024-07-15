"""
This module provides functionality to print the directory structure of a given path.
"""

import sys
import os
from pathlib import Path
from colorama import Fore

def print_path_structure(path):
    """
    Print the directory structure of a given path.

    Parameters:
    path (str): The path to the directory.

    Raises:
    FileNotFoundError: If the directory does not exist.
    """
    if not Path(path).is_dir():
        raise FileNotFoundError(f"The directory {path} does not exist.")
    return print_path_structure_from_dir(path)

def print_path_structure_from_dir(path):
    """
    Helper function to print the directory structure of a given path.

    Parameters:
    path (str): The Path object for the directory.
    """
    for root, _, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{Fore.BLUE}{os.path.basename(root)}{Fore.RESET}")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{Fore.LIGHTGREEN_EX}{f}{Fore.RESET}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    print_path_structure(sys.argv[1])
