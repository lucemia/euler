from utils import *

ps = {}
for i in range(2, 101):
    ps[i] = dict(prime_factors(i))

print ps

def test(n):
    rs = {}
    for i in range(2, n+1):
        for j in range(2, n+1):
            rs[(i, j)] = {k: ps[i][k]*j for k in ps[i]}

    return len({tuple(k.items()) for k in rs.values()})
    # return len(rs)

assert test(5) == 15
print test(100)
