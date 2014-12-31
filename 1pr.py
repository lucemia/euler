from itertools import combinations

def c(m):
    for x in xrange(1, len(m)+1):
        for ks in combinations(m, x):
            yield x, reduce(lambda i,j: i*j, ks, 1)


def count(n, muliples):
    n -= 1
    total = 0
    for i, m in c(muliples):
        total += (-1 if i % 2 == 0 else 1) * (m + (n / m) * m) * (n/m) / 2
        # print total, i, m
    return total

if __name__ == "__main__":
    assert count(10, (3,5)) == 23
    print count(20, (3, 5))
    print count(1000, (3,5))
