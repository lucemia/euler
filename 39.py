


p = {}

for i in range(3, 333):
    for j in range(i, 1000-i):
        k = (i**2 + j**2) ** .5
        if k < j:
            break

        if k == int(k):
            print i, j, k

            if i+j+k not in p:
                p[i+j+k] = []

            p[i+j+k].append((i,j,k))

def f(n):
    return len(p[n])

assert f(120) == 3

print max(p, key=lambda i: len(p[i]))
