import numpy as np
from collections import *
from itertools import *
SIZE = 1000000

def gen(n):
    mark = defaultdict(list)

    mark[0] = [1]
    mark[1] = [1]

    for i in xrange(n):
        if i < 2: continue
        # don't need to test more than n**.5
        # if i > n**.5: break

        if i == 2 or len(mark[i]) == 0:
            # yield i
            # only need to cross over p**2
            for j in range(i, n, i):
                mark[j].append(i)

    return mark

mark = gen(SIZE)

def sol(n):
    has = 0
    for i in xrange(SIZE):
        if len(mark[i]) == n:
            has += 1
            if has == n:
                return i-n + 1
        else:
            has = 0

assert sol(2) == 14
assert sol(3) == 644
print sol(4)
