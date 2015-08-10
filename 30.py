
def sol(n):
    total = 0
    for i in range(2, 355000):
        if sum(map(lambda i: int(i)**n, str(i))) == i:
            total += i

    return total

assert sol(4) == 19316
print sol(5)
