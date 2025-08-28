
from unittest.mock import patch
import cv2
from pac.pac_game import GameMaster

def test_quit():
    """when we quit the game, the game should be saved"""
    gm = GameMaster()
    with patch('cv2.waitKey', return_value=113):
        gm.handle_keyboard()
    assert gm.game.status == "exited"
