
def split(fs, ch):
    if not fs:
        if ch[0] and ch[1]:
            yield ch

    else:
        f = fs[0]

        for i in split(fs[1:], (ch[0] + [f], ch[1])):
            yield i

        for i in split(fs[1:], (ch[0], ch[1] + [f])):
            yield i


MUL = lambda v: reduce(lambda i,j: i*j, v, 1)

def test(fs, n):
    lower = 10**(n-1)
    upper = 10 ** (n)
    for a, b in split(fs, ([], [])):
        # print fs, n, a, b, MUL(a), MUL(b)
        if lower <= MUL(a) < upper and lower <= MUL(b) < upper:
            return True

    return False

def prime_factor(n):
    for i in xrange(2, n/2):
        if n % i == 0:
            f = [i]
            n /= i
            while n % i == 0:
                n /= i
                f.append(i)

            return f + prime_factor(n)

    return [n]

def sol(n):
    limit = 10**n
    for v in xrange(limit-1, 1, -1):
        rv = ''.join(reversed(str(v)))
        t = v * limit + int(rv)

        fs = prime_factor(t)
        if test(fs, n):
            return t

assert sol(2) == 9009
print sol(3)
 # print test(prime_factor(9009), 2)
