from sympy import *

def sol_gcd(f0, f1, n):
    q, f = div(f0, f1, n)

    if f == 0:
        return f1

    return sol_gcd(f1, f, n)

def fast_gcd(a, b):
    if a > b:
        a, b = b, a

    if b % a == 0:
        return a

    return fast_gcd(a, b%a)

a, b, n = symbols('a b n')

f0 = (n+a)**3 + b
f1 = n**3 + b

assert sol_gcd(f0, f1, n) == (a**6 + 27*b**2) / (4*a**3)
_gcd = sol_gcd(f0, f1, n)

# def count(va, vb):
#     value = _gcd.subs(a, va).subs(b, vb)
#     if value.is_integer:
#         test()
#     else:
#         p, q = value.p, value.q

def test(f0, f1, va, vb):
    cycle = _gcd.subs(a, va).subs(b, vb)
    if not cycle.is_integer:
        X = cycle.p
    else:
        X = cycle
    X *= va

    # print cycle, va, vb, cycle
    v = []
    for i in xrange(X):
    #     x = (i+va)**3 + vb
    #     y = i**3 + vb
    #     if x % cycle == 0 and y % cycle == 0:
    #         return i

    # raise
        g = fast_gcd((i+va)**3+vb, i**3+vb)
        g = gcd(f0.subs(a, va).subs(b, vb).subs(n, i), f1.subs(a, va).subs(b, vb).subs(n, i))
        v.append(g)

    BIG = max(v)
    print va, vb, BIG, cycle, X
    factors = [k for k, x in enumerate(v) if x == BIG]
    # # print va, vb, factors[0], cycle
    return factors[0]
    # print BIG, min(factors), factors[1] - factors[0], factors

def sol(a, b):
    total = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            total += test(f0, f1, i, j)

    return total

# print test(f0, f1, 10, 1)
assert test(f0, f1, 1, 1) == 5
assert test(f0, f1, 2, 1) == 101
assert sol(5, 5) == 128878
# assert sol(10, 10) == 32936544
# print sol(18, 1900)
