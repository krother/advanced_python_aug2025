"""
Data model of the core game classes
"""
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from pac.config import UP, DOWN, LEFT, RIGHT
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


class MoveStrategy(ABC):
    """like an interface or abstract class, we do not want this to be instantiated"""
    
    @abstractmethod
    def get_next_direction(self) -> Vector:
        pass


class RandomMoveStrategy(MoveStrategy):

    def get_next_direction(self) -> Vector:
        return random.choice([UP, DOWN, LEFT, RIGHT])


class LeftRightMoveStrategy(MoveStrategy):

    def __init__(self):
        self.counter = 0

    def get_next_direction(self) -> Vector:
        self.counter += 1
        if self.counter <= 5:
            return LEFT
        elif self.counter < 10:
            return RIGHT
        else:
            self.counter = 0
            return RIGHT


@dataclass
class Ghost(Character):
    color: str
    move_strategy: MoveStrategy

    def move(self, game):
        self.direction = self.move_strategy.get_next_direction()
        super().move(game)  # calls move() of Character or whatever the superclass is

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
