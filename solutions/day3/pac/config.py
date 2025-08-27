
import os

from pac.vector import Vector

WINDOW_TITLE = "Pac"
TILE_FILE = os.path.split(__file__)[0] + "/tiles.png"

# constants measured in pixels
SCREEN_SIZE_X, SCREEN_SIZE_Y = 640, 640
TILE_SIZE = 32

UP = Vector(x=0, y=-1)
DOWN = Vector(x=0, y=1)
LEFT = Vector(x=-1, y=0)
RIGHT = Vector(x=1, y=0)

# map keyboard keys to move commands
MOVES = {
    "a": LEFT,
    "d": RIGHT,
    "w": UP,
    "s": DOWN,
}

TILE_NAMES = {"#": "wall", ".": "dot", " ": "floor"}
