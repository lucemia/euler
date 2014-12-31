
results = {1:1}

def step(n):
    if n in results:
        return results[n]

    if n % 2 == 0:
        results[n] = step(n/2) + 1
        return results[n]

    results[n] = step(3*n+1) + 1
    return results[n]


def sol(n):
    big = 0
    index = 0
    for i in xrange(1, n):
        current = step(i)
        if current > big:
            big = current
            index = i

    return index

# print step(13), results
assert step(13) == 10

print sol(1000000)
