# f(2) = (a+b)**2 - (a**2 + b**2) = 2ab
# f(3) = (a+b+c)**2 - (a**2 + b**2 + c**2) = 2ab + 2bc + 2ac = f(2) + 2(a+b)*c
# ...

def sol(n):
    if n == 2:
        return 4

    return sol(n-1) + 2 * n * sum(xrange(n))

assert sol(10) == 2640
print sol(100)
