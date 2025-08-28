from typing import Final

import numpy as np
import cv2

from pac.config import TILE_FILE, TILE_NAMES, TILE_SIZE, TILE_FILE, WINDOW_TITLE, SCREEN_SIZE_X, SCREEN_SIZE_Y
from pac.pac_classes import PacGame


class TileFactory:
    """loads and creates tiles for graphics"""
    
    def __init__(self):
        self.tiles = self.read_images()

    def get_tile(self, tile_name: str) -> np.ndarray:
        return self.tiles[tile_name]

    @staticmethod
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


factory: Final[TileFactory] = TileFactory()


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
    frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = factory.get_tile(tile)


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


