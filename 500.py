
def sol(n):
    return reduce(lambda i, j: i*(j+2) % 500500507, xrange(n), 1)
    # if n > 0:
    #     return (n+1) * sol(n-1)
    # else:
    #     return 1

assert sol(4) == 120
print sol(500500)
