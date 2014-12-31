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
            # yield i
            # only need to cross over p**2
            for j in range(i**2, n, i):
                mark[j] = 1

    return mark

mark = gen(1000000)

def sol(n):
    longest = 1
    BIG = 0
    primes = []
    for i in range(n):
        if mark[i] == 0:
            primes.append(i)

    for i, p in enumerate(primes):
        for j in xrange(i+longest+1, len(primes)):
            print i, j, longest, BIG
            SUM = sum(primes[i:i+j])
            if SUM > n: break

            if mark[SUM] == 0:
                print i, j, primes[i:i+j], SUM

                longest = j
                BIG = SUM

    return BIG

assert sol(100) == 41
# assert count(41) == 6
assert sol(1000) == 953
# assert count(953) == 21
print sol(1000000)
