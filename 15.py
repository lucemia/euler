import numpy as np


def find(i, j, array):
    if array[i, j] > 0:
        return array[i, j]

    else:
        v = 0
        if i > 0:
            v += find(i-1, j, array)
        if j > 0:
            v += find(i, j-1, array)
        array[i, j] = v
        return v

def sol(n):
    array =  np.zeros((n+1, n+1))
    array[0, 0] = 1

    return find(n, n, array)

assert sol(2) == 6
print sol(20)
