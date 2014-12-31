# python float has limit
def fn(n):
    return (((1 + 5**.5) / 2)**n - ((1-5**.5) / 2)**n) / (5**.5)


def sol(n):
    M = 10**(n-1)
    a = 1
    b = 1
    for i in xrange(3, 10000):
        a, b = b, a+b
        if b > M:
            return i

assert sol(3)==12
print sol(1000)
