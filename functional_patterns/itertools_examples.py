
# you find lots of generators in the itertools module
from itertools import cycle, permutations

c = cycle("ABC")
print([next(c) for i in range(10)])

#p = permutations("ABC")
#print(list(p))
