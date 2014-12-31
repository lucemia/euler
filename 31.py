

def sol(n, coins=(1, 2, 5, 10, 20, 50, 100, 200)):
    if n == 0:
        return 1

    coins = [k for k in coins if k <= n]
    choose = coins[-1]
    if choose == 1:
        return 1

    i = 0
    total = 0

    while i <= n:
        total += sol(n-i, coins[:-1])
        i += choose

    return total


assert sol(1) == 1
assert sol(2) == 2
print sol(200)
