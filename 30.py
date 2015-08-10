
def sol(n):
    total = 0
    for i in range(10**(n-1), 10 ** n):
        if sum(map(lambda i: int(i)**n, str(i))) == i:
            print i
            total += i

    return total

assert sol(4) == 19316
print sol(5)
