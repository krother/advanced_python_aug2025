"""
Factorial with threads
# adopted from
http://www.devshed.com/c/a/Python/Basic-Threading-in-Python/1/
"""

# GIL: Global Interpreter Lock

import threading
import time
import random
from functools import cache


class FibonacciThread(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    @staticmethod
    @cache
    def fibo(n):
        if n < 2:
            return n
        else:
            return FibonacciThread.fibo(n - 2) + FibonacciThread.fibo(n - 1)

    def run(self):
        result = self.fibo(self.number)
        time.sleep(random.randint(5, 10))  # returns control to interpreter
        print(f"fibonacci({self.number}) = {result}")


for number in range(10):
    FibonacciThread(number).start()  # calls run()
