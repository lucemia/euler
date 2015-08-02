from utils import *
import numpy as np

def isabundant(n):
    fs = prime_factors(n)
    total = 1
    for f, c in fs:
        a = 0
        for i in range(c+1):
            a += f**i

        total *= a

    return total-n > n

assert not isabundant(8)
assert isabundant(12)
assert not isabundant(11)

abundant = set()
for i in xrange(1, 28124):
    if isabundant(i):
        abundant.add(i)


def test(n):
    for i in abundant:
        if i > n: continue
        if n-i in abundant:
            return True

    return False


assert test(24)
total = 0
for i in xrange(1, 28124):
    if not test(i):
        total += i

print total
