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

    # print total - n
    return total-n > n

assert not isabundant(28)
assert not isabundant(8)
assert isabundant(12)
for i in range(1, 12):
    assert not isabundant(i)

abundant = set()
for i in xrange(1, 28124):
    if isabundant(i):
        print i
        abundant.add(i)

# print len(abundant)

def test(n):
    for i in abundant:
        if i > n: continue
        if n-i in abundant:
            return True

    return False

assert test(24)
assert test(28150)

total = 0
for i in xrange(1, 28124):
    if not test(i):
        # print i
        total += i

print total
