import sys
import time
import random

n = int(sys.argv[1])

a, b = 0, 1
while n > 0:
    a, b = b, a + b
    n -= 1

delay = random.randint(5, 15)
time.sleep(delay)
print(f"fibonacci({sys.argv[1]}) = {a} after {delay} sec")
