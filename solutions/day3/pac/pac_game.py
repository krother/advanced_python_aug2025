"""
A 2D game using OpenCV for graphics
"""
from typing import Final

import cv2
import numpy as np

from pac.vector import Vector
from pac.pac_classes import Pac, Ghost, Level, PacGame, RandomMoveStrategy, LeftRightMoveStrategy
from pac.config import TILE_FILE, WINDOW_TITLE, SCREEN_SIZE_X, SCREEN_SIZE_Y, MOVES, TILE_NAMES, TILE_SIZE
from pac.util import ticker



def read_images():
    """
    Reads an image with tiles and extracts slices for game elements
    """
    img = cv2.imread(TILE_FILE)
    if img is None:
        raise IOError(f"Image not found: '{TILE_FILE}'")
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
    frame: np.ndarray,
    x: int,
    y: int,
    tile: str,
    xbase: int = 0,
    ybase: int = 0,
):
    """convert grid position to screen position in pixels and draw tile"""
    xpos = xbase + x * TILE_SIZE
    ypos = ybase + y * TILE_SIZE
    frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = tile_images[tile]


def draw(game: PacGame) -> None:
    """creates and displays the content of the game window
    
    Args:
       game: an instance of a PacGame that is drawn

    Returns:
       nothing
    """
    frame = np.zeros(
        (SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8
    )  # empty screen

    # draw the level
    for y, row in enumerate(game.level.board):
        for x, element in enumerate(row):
            draw_tile(
                frame=frame, x=x, y=y, tile=TILE_NAMES.get(element, "floor")
            )

    # draw pac
    draw_tile(
        frame=frame,
        x=game.player.position.x,
        y=game.player.position.y,
        tile="player",
    )
    # draw ghosts
    for g in game.ghosts:
        draw_tile(
            frame=frame,
            x=g.position.x,
            y=g.position.y,
            tile="ghost_" + g.color,
        )

    cv2.imshow(WINDOW_TITLE, frame)  # display complete image


def handle_keyboard(game):
    """keys are mapped to move commands"""
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "q":
        game.status = "exited"
    move = MOVES.get(key)
    if move:
        game.player.direction = move


def main():
    game = PacGame(
        player=Pac(
            direction=Vector(0, 0),
            position=Vector(1, 1),
            score=0,
        ),
        ghosts=[
            Ghost(direction=Vector(1, 0),
                  position=Vector(10, 1),
                  color="red",
                  move_strategy=RandomMoveStrategy()
                  ),
            Ghost(direction=Vector(1, 0),
                  position=Vector(1, 9),
                  color="blue",
                  move_strategy=LeftRightMoveStrategy()
                  ),
        ],
        level=Level(
            level="""
    #################
    #...............#
    #.###.#####.###.#
    #.#...#...#...#.#
    #...#...#.x.#...#
    #.#...#####...#.#
    #...#...#...#...#
    #.#...#...#...#.#
    #.###.#####.###.#
    #...............#
    #################"""
        ),
    )
    t = ticker(delta=0.2)
    while game.running:
        draw(game)
        handle_keyboard(game)
        if next(t):
            game.player.move(game)  # SHOULD IT LOOK LIKE THIS???
            for g in game.ghosts:
                g.move(game)

    cv2.destroyAllWindows()


tile_images: Final[dict[str, np.ndarray]] = read_images()


if __name__ == "__main__":
    main()
