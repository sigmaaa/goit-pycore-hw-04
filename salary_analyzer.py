"""
This module provides functionality to calculate the total and average salary from a CSV file.
The CSV file is expected to have the salary in the second column (index 1).
"""
from pathlib import Path
from decimal import Decimal, InvalidOperation
import csv

CSV_SALARY_INDEX = 1


def total_salary(path):
    """
    Calculate the total and average salary from a CSV file.

    Parameters:
    path (str): The path to the CSV file.

    Returns:
    tuple[Decimal, Decimal]: A tuple containing the total salary and the average salary.

    Raises:
    FileNotFoundError: If the file does not exist.
    IndexError: If a row in the CSV does not have enough columns.
    ValueError: If a salary value cannot be converted to an integer.
    """
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"The file {path} does not exist.")
    return calculate_total_salary_from_csv_file(path)


def calculate_total_salary_from_csv_file(path):
    """
    Helper function to calculate total and average salary from a CSV file.

    Parameters:
    path (Path): The Path object for the CSV file.

    Returns:
    tuple[Decimal, Decimal]: A tuple containing the total salary and the average salary.

    Raises:
    IndexError: If a row in the CSV does not have enough columns.
    ValueError: If a salary value cannot be converted to an integer.
    """
    total_salary_result = 0
    salaries = []

    with path.open(mode="r", encoding="UTF-8") as fr:
        reader = csv.reader(fr)
        for row in reader:
            if len(row) < 2:
                raise IndexError(f"Row {row} does not contain enough columns.")
            try:
                salary = Decimal(row[CSV_SALARY_INDEX])
            except InvalidOperation as exc:
                raise ValueError(f"Cannot convert {
                                 row[CSV_SALARY_INDEX]} to a Decimal.") from exc

            salaries.append(salary)
            total_salary_result += salary

    if not salaries:
        return (Decimal('0'), Decimal('0'))

    average_salary = total_salary_result / len(salaries)
    return (total_salary_result, average_salary)
