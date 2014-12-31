import numpy as np

SIZE = 1000000

def sol(n):
    mark = np.zeros(SIZE)
    for i in xrange(SIZE):
        if i < 2: continue
        if i == 2 or mark[i] == 0:
            for j in range(SIZE/i):
                mark[j*i] = 1

            n -= 1

            if n == 0:
                return i

assert sol(6) == 13
print sol(10001)
