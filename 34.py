def N(n):
    if n <= 1: return 1
    return n*N(n-1)

X = []
for i in range(10):
    X.append(N(i))

def test(n):
    return n == sum(X[int(k)] for k in str(n))

assert test(145)

total = 0
for i in range(10, 10000000):
    if test(i):
        total += i
        print total

print total
