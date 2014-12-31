import numpy as np

SIZE = 2000000

def gen(n):
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

    return mark

# x^2 - y^2 + a(x-y) = (x-y)(x+y) + a(x-y) = (x+y+a)

def count(a, b, primes):
    if primes[b] == 1: return 0

    current = b
    for n in xrange(1, 1000):
        current += a + n + n - 1
        if primes[current] == 1:
            return n

def sol(n, primes):
    BIG = 0
    best = None
    for a in range(-n+1, n):
        for b in range(-n+1, n):
            x = count(a, b, primes)
            if x > BIG:
                BIG = x
                best = (a, b)

    return best

primes = gen(SIZE)
assert count(1, 41, primes) == 40
assert count(-79, 1601, primes) == 80
print sol(1000, primes)
