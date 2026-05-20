"""
Module: student
Task 1: School class management with CSV / pickle serialization.
Variant 19: average birthday, search by surname.
"""

import csv
import pickle
import os
from typing import List


class Student:
    """Student with surname, initials, and birth date."""

    def __init__(self, surname: str, initials: str, day: int, month: int, year: int):
        self.surname = surname
        self.initials = initials
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{self.surname} {self.initials}: {self.day:02d}.{self.month:02d}.{self.year}"

    def to_list(self) -> List:
        return [self.surname, self.initials, self.day, self.month, self.year]

    @classmethod
    def from_list(cls, data: List):
        return cls(data[0], data[1], int(data[2]), int(data[3]), int(data[4]))


def save_csv(students: List[Student], path: str) -> None:
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Surname', 'Initials', 'Day', 'Month', 'Year'])
        for s in students:
            writer.writerow(s.to_list())


def load_csv(path: str) -> List[Student]:
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        return [Student.from_list(row) for row in reader if row]


def save_pickle(students: List[Student], path: str) -> None:
    with open(path, 'wb') as f:
        pickle.dump(students, f)


def load_pickle(path: str) -> List[Student]:
    if not os.path.exists(path):
        return []
    with open(path, 'rb') as f:
        return pickle.load(f)


def avg_birthday(students: List[Student]) -> tuple:
    if not students:
        return 0.0, 0.0, 0.0
    n = len(students)
    return (sum(s.day for s in students) / n,
            sum(s.month for s in students) / n,
            sum(s.year for s in students) / n)


def find_by_surname(students: List[Student], surname: str) -> Student:
    for s in students:
        if s.surname.lower() == surname.lower():
            return s
    raise ValueError(f"Student '{surname}' not found")


def input_student() -> Student:
    while True:
        try:
            surname = input("Surname: ").strip()
            initials = input("Initials: ").strip()
            day = int(input("Day (1-31): "))
            month = int(input("Month (1-12): "))
            year = int(input("Year: "))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2025):
                raise ValueError("Invalid date")
            return Student(surname, initials, day, month, year)
        except Exception as e:
            print(f"Input error: {e}. Try again.")


def main_student_cli():
    students = []
    csv_path = "data/students.csv"
    pkl_path = "data/students.pkl"

    while True:
        print("\n=== Task 1: School class ===")
        print("1. Add student")
        print("2. Show all")
        print("3. Save CSV")
        print("4. Load CSV")
        print("5. Save pickle")
        print("6. Load pickle")
        print("7. Average birthday")
        print("8. Find by surname")
        print("0. Back")
        cmd = input("Choice: ")

        if cmd == '1':
            students.append(input_student())
        elif cmd == '2':
            for s in students:
                print(s)
        elif cmd == '3':
            save_csv(students, csv_path)
            print("Saved CSV")
        elif cmd == '4':
            students = load_csv(csv_path)
            print(f"Loaded {len(students)} from CSV")
        elif cmd == '5':
            save_pickle(students, pkl_path)
            print("Saved pickle")
        elif cmd == '6':
            students = load_pickle(pkl_path)
            print(f"Loaded {len(students)} from pickle")
        elif cmd == '7':
            d, m, y = avg_birthday(students)
            print(f"Average birthday: {d:.2f}.{m:.2f}.{y:.2f}")
        elif cmd == '8':
            name = input("Surname to find: ")
            try:
                print(find_by_surname(students, name))
            except ValueError as e:
                print(e)
        elif cmd == '0':
            break