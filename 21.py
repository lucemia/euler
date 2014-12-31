import numpy as np
from collections import *

factors = {}
def prime_factor(n):
    f = Counter()
    for i in xrange(2, int(n**.5)+1):
        if n in factors:
            f.update(factors[n])
            return f

        while n % i == 0:
            f[i] += 1
            n /= i

    f[n] += 1

    if 1 in f:
        f.pop(1)

    return f

def gs(a, r, n):
    if r == 1:
        return a * n

    return a * (r**n - 1) / (r-1)

array = None

def count(n):

    f = prime_factor(n)
    total = 1
    for i in f:
        total *= gs(1, i, f[i]+1)

    v = total - n
    return v

def test(i):
    c = count(i)
    if c!= i and count(c) == i:
        return True

    return False

def sol(n):
    total = 0
    for i in xrange(2, n+1):
        if test(i):
            print i
            total += i

    return total

assert count(220) == 284
assert count(284) == 220
assert test(220) and test(284)
print sol(10000)
