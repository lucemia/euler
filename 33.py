from utils import *

def is_curious(a, b):
    r = float(a) / b

    aa = [a / 10, a % 10]
    bb = [b / 10, b % 10]

    for i in range(2):
        for j in range(2):
            if aa[i] == bb[j]:
                if aa[i] == 0: continue
                if bb[1-j] == 0: continue
                if float(aa[1-i]) / bb[1-j] == r:
                    # if a % aa[1-i] != 0:
                    return True

    return False

assert is_curious(49, 98)
v = []
for i in range(10, 100):
    for j in range(i+1, 100):
        if is_curious(i, j):
            print i, j
            v.append((i, j))

assert len(v) == 4

numerator = reduce(lambda i,j: i*j[0], v, 1)
denominator = reduce(lambda i,j: i*j[1], v, 1)

print numerator, denominator
