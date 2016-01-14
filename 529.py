import numpy


def test(n):
    ds = map(int, str(n))
    l = len(ds)
    a = numpy.zeros(shape=(l, l))

    pos = set()
    for k in xrange(10):
        for i in range(k, l):
            if k == 0:
                a[k, i] = ds[i]
                continue

            # if a[k-1, i-1] >= 10:
            #     continue

            a[k, i] = a[k-1, i-1] + ds[i]
            if a[k, i] == 10:
                pos.update(range(i-k, i+1))

    # print pos
    # print a
    return len(pos) == l


def T(n):
    c = 0
    for i in range(10**n):
        if test(i):
            # print i
            c += 1

    return c

assert T(2) == 9
print T(3), T(4)
assert T(5) == 3492
assert test(3523014)
assert not test(28546)
