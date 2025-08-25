
# Generator Exercise

## 1. Ticker

Run the code in [ticker.py](ticker.py). Understand what it does.

## 2. Slow down the game

Use the ticker in the main loop of the game to slow down the movement.
Follow these steps:

- place the ticker function in the code
- create a new ticker with a delta of 0.1 before the `while` loop.
- inside the loop, use `next()` to retrieve the next value from the ticker.
- move the pac only if the tick value is `True`
- experiment with the 

## 3. Ghost Movement

Write a generator function `random_moves()` that produces an endless sequence of random directions using `yield`. 
Make the code in [ghost_move.py](ghost_move.py) work.

**The lines are complete and correct, but the order is wrong and indentation is missing.**

Integrate the code into your game.

## 4. Regular Ghost

Write another move generator that moves 5 times left, then 5 times right and then repeats.
