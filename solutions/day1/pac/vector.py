from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

@dataclass
class Vector:
    x: int
    y: int

    def __len__(self):
        return round(sqrt(self.x**2 + self.y**2))

    def __repr__(self) -> str:
        """
        used when printing vectors that are inside lists, dicts or other structures,
        error messages and when there is no __str__ method
        """
        return f"{self.x}/{self.y}"

    def __str__(self) -> str:
        """used when printing directly or string conversion"""
        return f"Vector: x={self.x} y={self.y}"
    
    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __eq__(self, other: Vector) -> bool:
        return self.x == other.x and self.y == other.y 
    
    def __lt__(self, other: Vector) -> bool:
        return len(self) < len(other)


if __name__ == "__main__":
    v1 = Vector(x=3, y=4)
    v2 = Vector(x=1, y=2)
    v3 = Vector(x=3, y=4)
    v4 = Vector(x=2, y=7)
    print(v1)
    print(v1.x)
    print("Len:", len(v1))
    print([v1, v2])

    print(v1 + v2)
    print(f"Eq: ", v1 == v3)
    print(f"Eq: ", v1 == v2)

    data = [v1, v2, v3, v4]
    data.sort()
    print(data)
