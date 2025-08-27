@dataclass
class Ghost:
def random_move() -> Generator[str, None, None]:
def move(self):
direction = next(self.move_gen)
for _ in range(10):
g = Ghost(move_gen=random_move())
g.move()
from typing import Generator
from dataclasses import dataclass
import random
move = random.choice(["up", "down", "left", "right"])
move_gen: Generator[str, None, None]
print(f"now the ghost is moving {direction}")
while True:
yield move
