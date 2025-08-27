import time


def ticker(delta:float):
    """yields True if 'delta' seconds passed since the last tick."""
    last = time.time()  # processor time in seconds
    while True:
        current = time.time()
        if current - last >= delta:
            last = current
            yield True
        else:
            yield False

