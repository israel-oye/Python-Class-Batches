# import arithmetic_operators, math, random, functools
# from arithmetic_operators import add
from math import *  # NEVER DO A WILDCARD IMPORT

import arithmetic_operators as ops
import data

total = ops.add(10, 11)
# total_ = add(12, 13)
print(cos(45))
print(data.names)

for name in data.names:
    print(name.lower())