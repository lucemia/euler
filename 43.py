

def check(n):
    n = str(n)

    if int(n[1:4]) % 2 != 0:
        return False
    if int(n[2:5]) % 3 != 0:
        return False
    if int(n[3:6]) % 5 != 0:
        return False
    if int(n[4:7]) % 7 != 0:
        return False
    if int(n[5:8]) % 11 != 0:
        return False
    if int(n[6:9]) % 13 != 0:
        return False
    if int(n[7:10]) % 17 != 0:
        return False

    return True


def x(n):
    for i in range(1, 1000/n+1):
        if (n*i) >= 1000:
            break
        yield n*i

def f(m=[17, 13, 11, 7, 5, 3, 2], s=""):
    if not m:
        miss = [k for k in range(10) if str(k) not in s][0]
        print miss
        if miss != 0:
            yield int(str(miss) + s)
        return

    q = m[0]

    # print q, s
    if not m:
        return

    if not s:
        for i in x(q):
            n = str(i)
            if len(n) == 1: continue
            if len(n) == 2:
                n = "0" + n
            if len(set(n)) != 3: continue

            for j in f(m[1:], n):
                yield j

    else:
        for j in range(10):
            if str(j) not in s and int(str(j)+s[:2]) % q == 0:
                for k in f(m[1:], str(j) + s):
                    yield k

Y = list(f())

assert 1406357289 in Y
assert check(1406357289)
for i in Y:
    check(i)

print sum(Y)
