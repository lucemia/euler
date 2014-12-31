
import numpy as np

def sol(v):
    v = [map(int, k.split()) for k in v.split('\n') if k.strip()]
    n = len(v)

    array = np.zeros((n,n))

    for i in reversed(xrange(0, n)):
        for j in xrange(0, i+1):
            if i == n-1:
                array[i, j] = v[i][j]
            else:
                array[i, j] = v[i][j] + max(array[i+1,j], array[i+1,j+1])

    # print array
    return array[0][0]


v = open('p067_triangle.txt').read()
print sol(v)
