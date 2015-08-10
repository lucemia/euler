
def d(n):
    c = []
    m = []
    x = 10

    while True:
        if n > x:
            x *= 10
            c.append(0)
            m.append(None)
            continue

        nc = x / n
        nm = x % n
        x = nm * 10

        if nm == 0: return 0

        # print m, c
        if nm in m:
            return len(m) - m.index(nm)

        c.append(nc)
        m.append(nm)

assert d(2) == 0
assert d(3) == 1
assert d(4) == 0
assert d(5) == 0
assert d(6) == 1
assert d(7) == 6
assert d(8) == 0
assert d(9) == 1
assert d(10) == 0

assert max(range(2, 10), key=d) == 7
print max(xrange(2, 1000), key=d)
