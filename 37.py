import numpy as np
from collections import *
from itertools import *
SIZE = 1000000

def gen(n):
    mark = np.zeros(SIZE)
    mark[0] = 1
    mark[1] = 1
    for i in xrange(n):
        if i < 2: continue
        # don't need to test more than n**.5
        if i > n**.5: break

        if i == 2 or mark[i] == 0:
            # yield i
            # only need to cross over p**2
            for j in range(i**2, n, i):
                mark[j] = 1

    return mark

mark = gen(SIZE)
primes = set(k for k in xrange(SIZE) if mark[k] == 0)

def test(n):
    str_n = str(n)
    if n not in primes: return False
    if len(str_n) == 1: return False

    for i in range(1, len(str_n)):
        if int(str_n[i:]) not in primes or int(str_n[:-i]) not in primes:
            return False

    return True

assert test(3797)

index = 0
total = 0
for i in primes:
    if test(i):
        print index, i
        total += i
        index += 1

print total
