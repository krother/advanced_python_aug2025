"""
A 2D game using OpenCV for graphics
"""
import cv2

from pac.vector import Vector
from pac.pac_classes import Pac, Ghost, Level, PacGame, RandomMoveStrategy, LeftRightMoveStrategy
from pac.config import MOVES
from pac.util import ticker
from pac.tiles import draw
from pac.repository import Repository


class GameMaster:

    def __init__(self):
        self.repo = Repository()
        self.game = self.start_game()

    def start_game(self):
        return PacGame(
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

    def handle_keyboard(self):
        """keys are mapped to move commands"""
        key = chr(cv2.waitKey(1) & 0xFF)
        if key == "q":
            self.repo.write(self.game)
            self.game.status = "exited"

        elif key == "l":
            self.game = self.repo.read()
        move = MOVES.get(key)
        if move:
            self.game.player.direction = move

    def run(self):
        t = ticker(delta=0.2)
        while self.game.running:
            draw(self.game)
            self.handle_keyboard()
            if next(t):
                self.game.player.move(self.game)  # SHOULD IT LOOK LIKE THIS???
                for g in self.game.ghosts:
                    g.move(self.game)


def main():
    gm = GameMaster()
    gm.run()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
