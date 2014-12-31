# (1+n)*n/2

# 1*2
# 2*3 4 / 2
# 3*4 (1,3) * (1,2,4) -1
# 4*5 (2) * 2
# 5*6 (1,5, 1, 2, 3)


from collections import Counter

factors = {}
def prime_factor(n):
    f = Counter()
    for i in xrange(2, int(n**.5)+1):
        if n in factors:
            f.update(factors[n])
            return f

        while n % i == 0:
            f[i] += 1
            n /= i

    f[n] += 1
    return f

MUL = lambda v: reduce(lambda i,j: i*j, v, 1)


def sol(n):
    for i in xrange(1, 100000):
        a = prime_factor(i)
        factors[i] = a
        b = prime_factor(i+1)
        factors[i+1] = b

        f = a + b
        f[2] -= 1
        if 1 in f:
            f.pop(1)

        r = MUL(k+1 for k in f.values() if k > 0)
        # print i, f, r
        if r > n:
            return i * (i+1) / 2

assert sol(5) == 28
print sol(500)
