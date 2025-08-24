
x = 10

def add(a: int, b: list[int], c: int=3, *args, **kwargs) -> int:
    # global x
    x = 5
    b.append(9)
    return a + sum(b) + c + sum(args) + sum(kwargs.values())

y = [2, 3, 4]
print(add(1, y, 5, 6, 7, z=8))
print(x)
print(y)