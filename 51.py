import numpy as np
from collections import *
from itertools import *
SIZE = 10000

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

def test(x):
    sub = defaultdict(list)

    for a, b in combinations(x, 2):
        sub[b-a].append((a,b))

    for k in sub:
        if len(sub[k]) == 2:
            items = set()
            for a, b in sub[k]:
                items.add(a)
                items.add(b)

            if len(items) == 3:
                print sub[k]
                return True

    # print sub


mark = gen(10000)
primes = [k for k in xrange(1000, 10000) if mark[k] == 0]

assert test([1487, 4817, 8147])

x = defaultdict(list)

for p in primes:
    c = Counter(str(p))
    i = list(c.items())
    i.sort()
    i = tuple(i)
    x[i].append(p)

for i in x:
    if len(x[i]) > 2:
        #print i, x[i]
        r = test(x[i])
        if r:
            print r
