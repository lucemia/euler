import numpy as np
from collections import *
from itertools import *
SIZE = 10000000

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
primes = reversed([k for k in xrange(SIZE) if mark[k] == 0])

# because 1-9 = 45 (will be 3 defactor)
# because 1-8 = 36 ..
#  1-6, 1-5 1-3

# only (1-7), 1-4 is possible

def test(n):
    len_ = len(str(n))

    if len_ not in (4, 7): return False

    target = set(range(1,len_ + 1))

    if 10**(len_ -1) < n < 10**len_:
        if set([int(k) for k in str(n)]) == target:
            return True

    return False

assert test(2143)

for p in primes:
    if test(p): print p
