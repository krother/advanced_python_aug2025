Decorator Classes
=================

In general, **decorators are functions that manipulate functions**. More
specifically, a decorator wraps a function to add extra behavior to a
function call. In the examples below, we will decorate a Python function
that calculates fibonacci numbers.

Example: you would like to print a timestamp at every function call. You could define a new
function:

``` {.sourceCode .python3}
import time

def fibonacci_with_timestamp(n):
    print(time.asctime())
    return fibonacci(n)
```

If you want to **add the timestamp feature to many functions**, consider
using a decorator:

``` {.sourceCode .python3}
class Timestamp:

    def __init__(self, message):
        self.message = message
        self.function = None

    def __call__(self, func):
        self.function = func
        return self.print_timestamp

    def print_timestamp(self, *args, **kwargs):
        print(time.asctime())            # done before addition
        result = func(*args, **kwargs)   # calls the addition function
        print(self.message)              # actions after addition
        return result


@Timestamp("Fibonacci function called")
def fibonacci(n):
    """Recursively calculates fibonacci numbers"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

You can argue that this does not simplify the code. Decorators pays off
in bigger programs, when they are used often. Logging function calls is
a good example for using a decorator.

----

Built-in decorators
-------------------

Most of the time, you will use built-in decorators. One example is
`functools.lru_cache` that memorizes the output of a function to save
time later. Let\'s decorate a function with it:

``` {.sourceCode .python3}
from functools import cache

@cache
def fibonacci(n):
    """Recursively calculates fibonacci numbers"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

Try calculating a recursive fibonacci number for `n=50` without the
decorator. It takes forever! By default, `cache` memorizes the intermediate results, so that the recursive fibonacci becomes slow again.

Built-in decorators are also used in:

-   web frameworks like **Flask** and **FastAPI** to assign URLs to Python functions
-   the **pytest** framework to create compact test code
-   classes with `@property` and `@staticmethod`
