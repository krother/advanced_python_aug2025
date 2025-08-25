"""
Data model implementation using TypedDict
(clean way to create type-annotated dictionaries for type checking
but no methods can be added)
"""
from typing import TypedDict
from pprint import pprint

class Level(TypedDict):    
    board: list[list[str]]

class Pac(TypedDict):
    direction: tuple [int, int]
    position: tuple [int, int]
    score: int

class Ghost (TypedDict):
    direction: tuple [int, int]
    position: tuple [int, int]
    color: str

class PacGame (TypedDict):
    player: Pac
    ghosts: list[Ghost]
    level: Level



def create_level(level: str) -> Level:
    level_matrix = [list(row) for row in level.strip().split()]
    return Level(level=level_matrix)


def print_level(level: Level) -> None:
    print("\n".join("".join(row) for row in level["level"]))

game = PacGame(
    player = Pac(
        direction= (1,0),
        position= (2,2),
        score= 0
    ),
    ghosts = [],
    level = create_level(level="""
#############
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#...........#
#############""",
))
print(game)

#print(level_one["name"])
#print_level(level_one)
#print(type(level_one))
