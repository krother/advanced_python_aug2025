

def factorial():
    a, b = 1, 1
    while True:
        a *= b
        yield a
        b += 1

def square(x):
    return x ** 2

iterator = factorial()
next(iterator)

# n = [next(gen) for i in range(10)]

# generator expression
# sq = (square(n) for n in factorial())

# mapping
# m = map(square, factorial())
