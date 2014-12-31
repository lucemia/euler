from collections import Counter
def prime_factor(n):
    for i in xrange(2, n/2+1):
        if n % i == 0:
            f = [i]
            n /= i
            while n % i == 0:
                n /= i
                f.append(i)

            return f + prime_factor(n)

    return [n]

def sol(n):
    cs = []
    for i in xrange(1, n+1):
        c = Counter(prime_factor(i))
        cs.append(c)

    muls = set()
    for c in cs:
        muls.update(c.keys())

    total = 1
    for mul in muls:
        total *= (mul) ** (max(c[mul] for c in cs))

    return total

assert sol(10) == 2520
print sol(20)
