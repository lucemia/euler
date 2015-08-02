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

    Y = X
    X *= va

    v = []
    i = 0

    while True:
        if i > X: break
        x = (i+va)**3 + vb
        y = i**3 + vb

        if x % Y == 0 and y % Y == 0:
            v.append([i, gcd(x,y)])
            i += X
        else:
            i += 1

    print v
    v.sort(key=lambda i: (-i[1], i[0]))
    return v[0][0]

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
