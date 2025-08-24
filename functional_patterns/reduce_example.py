"""
Understand the following code
"""
import functools
import itertools


g = (
    functools.reduce(lambda a,b:a*b, range(1, x+1), 1)
    for x in itertools.count(1)
)
