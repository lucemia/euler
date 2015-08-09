import numpy as np
MAX_SIZE = 2000000



def prime_factors(n):
    i = 2
    fs = []
    while i <= n**.5:
        f = i
        c = 0
        while n % i == 0:
            c += 1
            n /= i
        if c > 0:
            fs.append((i, c))
        i += 1

    if n > 1:
        fs.append((n, 1))
    return fs

assert prime_factors(12) == [(2, 2), (3, 1)]

def gen(n):
    mark = np.zeros(MAX_SIZE)
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

    return mark
