
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
