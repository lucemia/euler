

def sol(n):
    if n == 1: return 1

    MAX = n**2 # ex 25, 21, 17, 13
    total = MAX + MAX - (n-1) + MAX - 2*(n-1) + MAX - 3*(n-1)
    return total + sol(n-2)

assert sol(1) == 1
assert sol(3) == sol(1) + 3+5+7+9
assert sol(5) == sol(3) + 13+17+21+25

print sol(1001)
