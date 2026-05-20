"""
Module: trapezoid
Task 4: Abstract GeometricFigure, FigureColor (property), IsoscelesTrapezoid, mixin example.
Variant 19: trapezoid with height h, base a, middle line b.
"""

from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class FigureColor:
    """Color property demo."""

    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str):
        self._color = value


class DrawableMixin:
    """Mixin for drawing ability."""

    def draw(self, ax=None):
        raise NotImplementedError


class GeometricFigure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class IsoscelesTrapezoid(GeometricFigure, DrawableMixin):
    figure_type = "IsoscelesTrapezoid"

    def __init__(self, h: float, a: float, b: float, color: FigureColor):
        self._h = h
        self._a = a
        self._b = b
        self._color = color
        self._validate()

    def _validate(self):
        if self._h <= 0 or self._a <= 0 or self._b <= 0:
            raise ValueError("Positive values required")
        if 2 * self._b - self._a <= 0:
            raise ValueError("Invalid second base")

    @property
    def other_base(self) -> float:
        return 2 * self._b - self._a

    def area(self) -> float:
        return self._h * self._b

    def vertices(self):
        a, b, h = self._a, self.other_base, self._h
        return [(-a / 2, 0), (a / 2, 0), (b / 2, h), (-b / 2, h)]

    def draw(self, ax=None, label=""):
        if ax is None:
            fig, ax = plt.subplots()
        verts = self.vertices()
        poly = patches.Polygon(verts, closed=True, edgecolor='black',
                               facecolor=self._color.color, alpha=0.7)
        ax.add_patch(poly)
        ax.set_xlim(-max(self._a, self.other_base) - 1, max(self._a, self.other_base) + 1)
        ax.set_ylim(-1, self._h + 1)
        ax.set_aspect('equal')
        ax.grid(True)
        if label:
            ax.text(0, self._h / 2, label, ha='center', va='center', fontsize=12,
                    bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
        return ax

    def __str__(self):
        return (f"{self.figure_type}: h={self._h}, a={self._a}, "
                f"b={self._b}, other_base={self.other_base:.2f}, "
                f"area={self.area():.2f}, color={self._color.color}")


def input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a number.")


def main_trapezoid_cli():
    print("\n=== Task 4: Isosceles Trapezoid (OOP) ===")
    try:
        h = input_float("Height h: ")
        a = input_float("Base a: ")
        b = input_float("Middle line b: ")
        color_name = input("Color (e.g., blue, green): ")
        trap = IsoscelesTrapezoid(h, a, b, FigureColor(color_name))
        print(trap)
        ax = trap.draw(label="My Trapezoid")
        plt.title("Isosceles Trapezoid")
        plt.savefig("plots/trapezoid.png")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")