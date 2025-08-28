"""manages persistence of pac games"""

import pickle

from dataclasses import asdict

from pac.pac_classes import PacGame


class Repository:

    def read(self) -> PacGame:
        return pickle.load(open("saved.pkl", "rb"))

    def write(self, game: PacGame) -> None:
        pickle.dump(game, open("saved.pkl", "wb"))
        #d = asdict(game)
        #print(d)
        
