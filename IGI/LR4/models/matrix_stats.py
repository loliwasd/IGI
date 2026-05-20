"""
Module: matrix_stats
Task 5: NumPy matrix — even/odd counts + correlation (numpy and manual).
Variant 19.
"""

import numpy as np


def random_int_matrix(rows: int, cols: int, low=-100, high=100):
    return np.random.randint(low, high, size=(rows, cols))


def count_even_odd(matrix: np.ndarray):
    evens = np.sum(matrix % 2 == 0)
    odds = matrix.size - evens
    return int(evens), int(odds)


def corrcoef_numpy(x, y):
    if len(x) < 2 or len(y) < 2:
        return 0.0
    return np.corrcoef(x, y)[0, 1]


def corrcoef_manual(x, y):
    n = len(x)
    if n < 2:
        return 0.0
    mx, my = sum(x) / n, sum(y) / n
    cov = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    sx = sum((xi - mx) ** 2 for xi in x) ** 0.5
    sy = sum((yi - my) ** 2 for yi in y) ** 0.5
    if sx == 0 or sy == 0:
        return 0.0
    return cov / (n * sx * sy)


def main_matrix_stats():
    print("\n=== Task 5: NumPy Matrix ===")
    r = int(input("Rows: "))
    c = int(input("Cols: "))
    M = random_int_matrix(r, c)
    print("Matrix:\n", M)

    ev, od = count_even_odd(M)
    print(f"Even: {ev}, Odd: {od}")

    flat = M.flatten()
    even_idx_vals = [flat[i] for i in range(0, len(flat), 2)]
    odd_idx_vals = [flat[i] for i in range(1, len(flat), 2)]
    min_len = min(len(even_idx_vals), len(odd_idx_vals))
    x = even_idx_vals[:min_len]
    y = odd_idx_vals[:min_len]

    if min_len >= 2:
        np_corr = corrcoef_numpy(x, y)
        manual_corr = corrcoef_manual(x, y)
        print(f"Correlation (numpy): {np_corr:.4f}")
        print(f"Correlation (manual): {manual_corr:.4f}")
    else:
        print("Not enough data for correlation")