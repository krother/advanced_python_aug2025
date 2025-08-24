"""
the items are better encapsulated
"""
def Stack():
    _items = []

    def push(item):
        _items.append(item)

    def pop():
        return _items.pop()

    def closure():
        pass

    closure.push = push
    closure.pop = pop
    return closure


stack = Stack()
stack.push(42)
stack.push(41)
print(stack.pop())

# stack.push.__closure__[0].cell_contents
