
import math
def d(n):
    i = 1
    offset = 0
    while True:
        l = i * (10 ** i - 10 ** (i-1))
        if n > offset + l:
            offset += l
            i += 1

        else:
            q = (n-offset) % i
            m = offset + math.ceil((n-offset) / float(i))
            # print m, q, offset
            return int(str(m)[(n-offset) % i])

def dforce(n):
    buf = ""
    for i in range(1, n+3):
        buf += str(i)
        if len(buf) > n:
            return int(buf[n-1])


assert d(12) == 1
assert d(1) == 1
assert d(2) == 2
assert d(13) == 1

assert dforce(12) == d(12)
assert dforce(1) == d(1)
assert dforce(2) == d(2)
assert dforce(13) == d(13)


x = 1
for i in xrange(7):
    print x, dforce(10**i)
    x *= dforce(10**i)

print x
