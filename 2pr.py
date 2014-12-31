# http://en.wikipedia.org/wiki/Fibonacci_number

def fn(n):
    return (((1 + 5**.5) / 2)**n - ((1-5**.5) / 2)**n) / (5**.5)

def limit(n):
    for i in xrange(1000):
        if fn(i) > n:
            return i

def sol():
    total = 0
    for i in xrange(1000):
        v = int(fn(i))

        if v % 2 == 0:
            if v >= 4000000:
                return total

            total += v

print sol()
