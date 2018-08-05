import example
from time import time


def slowFunc():
    a = 0
    for x in range(10000000):
        a+=x
    return x


t = time()

for x in range(10):
    slowFunc()

q2 = time()-t
print("normal python:",q2)

t = time()

for x in range(10):
    example.slowFuncCpp()

q1 = time()-t
print("cpp accelerated:",q1)

print("speedup:", q2/q1)

