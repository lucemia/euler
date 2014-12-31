
def count(n):
    if n == 1:
        return 1

    return n * count(n-1)

def sol(n):
    return sum(map(int, str(count(n))))

assert sol(10) == 27
print sol(100)
