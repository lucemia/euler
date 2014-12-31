
def sol(n):
    return sum(map(int, str(2 ** n)))

assert sol(15) == 26
print sol(1000)
