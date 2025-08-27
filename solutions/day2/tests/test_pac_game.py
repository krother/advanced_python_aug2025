import pytest

from pac import PacGame, Pac, Vector, Level


@pytest.fixture
def simple_game():
    """field full of dots (4x4)"""
    # 1. set up test data (fixture)
    # there is a small level with lots of dots.
    # the pac is in the top left corner (0/0)
    # the pac is facing right
    return PacGame(
        player=Pac(
            direction=Vector(1, 0),
            position=Vector(0, 0),
            score=0,
        ),
        ghosts=[],
        level=Level(
            level="""
....
....
....
...."""
        ),
    )


def test_move(simple_game):
    # 2. code under test: the pac moves
    simple_game.player.move(simple_game)

    # 3. assertions
    # check the new position of the pac, it should now be (1/0)
    assert simple_game.player.position == Vector(1, 0)


def test_blocked_by_wall(simple_game):
    simple_game.level.board[0][1] = "#"

    # 2. code under test: the pac moves
    simple_game.player.move(simple_game)

    # 3. assertions
    # check the new position of the pac, it should now be (1/0)
    assert simple_game.player.position == Vector(0, 0)
