"""
Data model of the core game classes
"""
from dataclasses import dataclass, field

from pac.vector import Vector


@dataclass
class Level:
    level: str
    board: list[list[str]] = field(init=False, repr=False)

    def __post_init__(self):
        self.board = [list(row) for row in self.level.strip().split()]

    def __repr__(self) -> str:
        return "\n".join(["".join(row) for row in self.board])


@dataclass
class Character:
    direction: Vector
    position: Vector

    #@LogMove("move done")
    def move(self, game):
        new_position = self.position + self.direction
        if game.level.board[new_position.y][new_position.x] != "#":
            self.position = new_position
        else:
            self.direction = Vector(x=0, y=0)


@dataclass
class Pac(Character):
    score: int


@dataclass
class Ghost(Character):
    color: str

    def move(self):
        super().move()  # calls move() of Character or whatever the superclass is
        self.direction = Vector(-self.direction.x, -self.direction.y)


@dataclass
class PacGame:
    player: Pac
    ghosts: list[Ghost]
    level: Level
    status: str = "running"

    @property
    def running(self) -> bool:
        # introduced while resolving #234
        return self.status == "running"
