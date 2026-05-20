"""
Module: math_series
Task 3: arccos(x) series, statistics (mean, median, std, variance, mode), matplotlib plot.
Variant 19: arccos(x) = pi/2 - arcsin(x)
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean, median, mode, stdev, variance
from typing import List, Tuple


def series_arccos(x: float, eps: float = 1e-8, max_iter: int = 500) -> Tuple[float, int]:
    if abs(x) > 1:
        raise ValueError("|x| <= 1 required")
    if abs(x) == 1:
        return math.acos(x), 1
    term = x
    arcsin_val = term
    n = 1
    while abs(term) > eps and n < max_iter:
        num = (2 * n - 1) ** 2
        den = (2 * n) * (2 * n + 1)
        term *= x * x * num / den
        arcsin_val += term
        n += 1
    return math.pi / 2 - arcsin_val, n


def series_for_range(x_vals: List[float], eps: float = 1e-8):
    series_vals = []
    math_vals = []
    for x in x_vals:
        try:
            sv, _ = series_arccos(x, eps)
            series_vals.append(sv)
        except:
            series_vals.append(float('nan'))
        math_vals.append(math.acos(x))
    return series_vals, math_vals


def stats_from_list(data: List[float]) -> dict:
    valid = [v for v in data if not math.isnan(v)]
    if len(valid) < 2:
        return {}
    return {
        'mean': mean(valid),
        'median': median(valid),
        'mode': mode(valid) if valid else None,
        'variance': variance(valid),
        'std': stdev(valid)
    }


def plot_comparison(x_vals, series_vals, math_vals, stats, save_path="plots/arccos_plot.png"):
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, series_vals, 'b-', label="Series arccos(x)", linewidth=2)
    plt.plot(x_vals, math_vals, 'r--', label="math.acos(x)", linewidth=2)
    plt.xlabel("x")
    plt.ylabel("arccos(x)")
    plt.title("Comparison of arccos(x) computation")
    plt.legend()
    plt.grid(True)

    text = f"Mean: {stats.get('mean',0):.4f}\nMedian: {stats.get('median',0):.4f}\nStd: {stats.get('std',0):.4f}"
    plt.gca().text(0.05, 0.95, text, transform=plt.gca().transAxes,
                   fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"Plot saved to {save_path}")


def main_math_series():
    print("\n=== Task 3: arccos(x) series + statistics + plot ===")
    x_vals = np.linspace(-0.9, 0.9, 50).tolist()
    series_vals, math_vals = series_for_range(x_vals)
    stat = stats_from_list(series_vals)
    print("Statistics for series values (valid only):")
    for k, v in stat.items():
        print(f"  {k}: {v}")
    plot_comparison(x_vals, series_vals, math_vals, stat)
    print("Table (first 5 values):")
    print(f"{'x':>8} {'Series':>12} {'math':>12}")
    for i in range(5):
        print(f"{x_vals[i]:8.4f} {series_vals[i]:12.6f} {math_vals[i]:12.6f}")