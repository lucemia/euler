
def sol(n):
    for c in xrange(n/2, 1, -1):
        for a in xrange(1, c):
            b = n - a - c
            if b < a: continue

            if a**2+b**2 == c**2:
                return a*b*c, a, b, c

assert sol(12) == 60
print sol(1000)
