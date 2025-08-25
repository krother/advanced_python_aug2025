"""
Pac game after adding:
- up-down keys working
- data model
- vector class
- replacing literal directions by vectors
- extracting Character superclass
"""

import os
import cv2
from dataclasses import dataclass, field
from typing import Final

import numpy as np

from vector import Vector

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

    def move(self):
        self.position += self.direction


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
class PacGame :
    player: Pac
    ghosts: list[Ghost]
    level: Level



def read_images():
    """
    Reads an image with tiles and extracts slices for game elements
    """
    img = cv2.imread(TILE_FILE)
    if img is None:
        raise IOError(f"Image not found: '{TILE_FILE}'")
    # img = np.kron(img, np.ones((2, 2, 1), dtype=img.dtype))  # double image size
    tiles = {
        "wall": img[0:32, 0:32],
        "floor": img[32:64, 0:32],
        "dot": img[64:96, 0:32],
        "player": img[96:128, 0:32],
        "ghost_green": img[128:160, 96:128],
        "ghost_blue": img[160:192, 96:128],
        "ghost_red": img[192:224, 96:128],
        "ghost_pink": img[224:256, 96:128],
    }
    return tiles


def draw_tile(
    frame: np.ndarray, x: int, y: int, tile: str, xbase: int = 0, ybase: int = 0
):
    """convert grid position to screen position in pixels and draw tile"""
    xpos = xbase + x * TILE_SIZE
    ypos = ybase + y * TILE_SIZE
    frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = tile_images[tile]


def draw(game):
    frame = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)  # empty screen
    draw_tile(frame=frame, x=game.player.position.x, y=game.player.position.y, tile="player")
    #draw_tile(frame=frame, x=1, y=2, tile="wall")
    #draw_tile(frame=frame, x=2, y=2, tile="dot")
    #draw_tile(frame=frame, x=3, y=2, tile="floor")
    #draw_tile(frame=frame, x=4, y=2, tile="ghost_green")
    #draw_tile(frame=frame, x=5, y=2, tile="ghost_blue")
    #draw_tile(frame=frame, x=6, y=2, tile="ghost_red")
    #draw_tile(frame=frame, x=7, y=2, tile="ghost_pink")
    cv2.imshow(WINDOW_TITLE, frame)  # display complete image


def handle_keyboard(game):
    """keys are mapped to move commands"""
    global game_status
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "q":
        game_status = "exited"
    move = MOVES.get(key)
    if move:
        game.player.direction = move


def main():
    game_status: str = "running"
    queued_move = None
    while game_status == "running":
        draw(game)
        queued_move = handle_keyboard(game)
        game.player.move()

    cv2.destroyAllWindows()


tile_images: Final[dict[str, np.ndarray]] = read_images()

game = PacGame(
    player = Pac(
        direction = Vector(0, 0),
        position = Vector(2, 2),
        score= 0,
    ),
    ghosts=[],
    level=Level(
        level="""
##########
#........#
#........#
#........#
#........#
#........#
#........#
#........#
#........#
#........#
##########""")
)

if __name__ == "__main__":
    main()
