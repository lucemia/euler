import numpy as np

SIZE = 2000000

def sol(n):
    mark = np.zeros(SIZE)
    mark[0] = 1
    mark[1] = 1
    for i in xrange(n):
        if i < 2: continue
        # don't need to test more than n**.5
        if i > n**.5: break

        if i == 2 or mark[i] == 0:
            # only need to cross over p**2
            for j in range(i**2, n, i):
                mark[j] = 1

    # print [k for k in xrange(n) if not mark[k]]
    return sum(k if not mark[k] else 0 for k in xrange(n))

# print sol(1000)
assert sol(10) == 17
print sol(2000000)
