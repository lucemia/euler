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

def test(i, mark):
    if i < 10: return True

    i = str(i)

    for j in xrange(1, len(i)):
        if mark[int(i[j:] + i[:j])] == 1:
            return False

    return True

def sol(n):
    total = 0
    mark = gen(n)

    for i in xrange(2, n):
        if mark[i] == 0:
            if test(i, mark):
                total += 1

    return total

assert sol(100) == 13
print sol(1000000)
