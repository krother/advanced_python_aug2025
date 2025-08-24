"""
Example of parallel execution with asyncio

see:
https://docs.python.org/3/library/asyncio-task.html
"""
import asyncio
import random
from functools import reduce


def fibo(data, count):
    a, b = data
    return b, a + b


async def fibonacci(number):
    """delayed calculation of fibonacci number"""
    result = reduce(fibo, range(number), (0, 1))
    delay = random.randint(5, 10)
    await asyncio.sleep(delay)   # see what happens without 'await'
    print(f"after {delay:2} seconds: fibonacci({number}) = {result[0]}")


async def main():
    # create concurrent tasks
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(fibonacci(i)))

    # wait for tasks to finish
    # (all have to be awaited)
    for t in tasks:
        await t


# run the toplevel async function
asyncio.run(main())
