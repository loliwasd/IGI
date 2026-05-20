"""
Laboratory work #4 — Main entry point
Imports and tests all modules
Version: 1.0
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.student import main_student_cli
from models.text_analyzer import main_text_analyzer
from models.math_series import main_math_series
from models.trapezoid import main_trapezoid_cli
from models.matrix_stats import main_matrix_stats
from models.pandas_tasks import main_pandas_cli


def main():
    print("\n===== LABORATORY WORK #4 (Variant 19) =====")

    while True:
        print("\nSelect task:")
        print("1. Task 1 — School class (CSV / pickle)")
        print("2. Task 2 — Regex text analysis + zip")
        print("3. Task 3 — arccos(x) series + statistics + matplotlib plot")
        print("4. Task 4 — OOP: Isosceles trapezoid (inheritance, properties)")
        print("5. Task 5 — NumPy: even/odd + correlation coefficient")
        print("6. Task B — Pandas: Series, DataFrame, StrokePrediciton")
        print("0. Exit")

        choice = input("Your choice: ").strip()

        if choice == '1':
            main_student_cli()
        elif choice == '2':
            main_text_analyzer()
        elif choice == '3':
            main_math_series()
        elif choice == '4':
            main_trapezoid_cli()
        elif choice == '5':
            main_matrix_stats()
        elif choice == '6':
            main_pandas_cli()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()