# -*- encoding=utf8 -*-
from a502 import g as g0

store = {}

def g(w, h, odd=True):
    # print w, h
    if w <= 0 or h <= 0:
        if odd: return 0
        return 1

    if not odd:
        return int((h+1)**w - g(w, h))

    try:
        return store[(w, h)]
    except:
        pass

    # 按照第一個 0 的位置進行 dp
    total = 0

    mid = w / 2 + 1

    for i in xrange(h+1):
        if i % 2:
            # i is odd
            total += g1(mid, h, i, True) * g1(w-mid+1, h, i, True)
            total += g1(mid, h, i, False) * g1(w-mid+1, h, i, False)
        else:
            total += g1(mid, h, i, True) * g1(w-mid+1, h, i, False)
            total += g1(mid, h, i, False) * g1(w-mid+1, h, i, True)

    store[(w,h)] = total
    return total


def F(w, h):
    return g(w, h-1) - g(w, h-2)


def g1(w, h, x, odd=True):
    if w <= 0 or h <= 0:
        if odd: return 0
        return 1

    if not odd:
        return int((h+1)**(w-1) - g1(w, h, x))

    try:
        return store[(w, h, x)]
    except:
        pass

    if w == 1:
        if x % 2 and odd:
            return 1
        return 0

    mid = w / 2 + 1

    total = 0
    for i in xrange(h+1):
        if i % 2:
            # i is odd
            total += g2(mid, h, x, i, True) * g1(w-mid+1, h, i, True)
            total += g2(mid, h, x, i, False) * g1(w-mid+1, h, i, False)
        else:
            total += g2(mid, h, x, i, True) * g1(w-mid+1, h, i, False)
            total += g2(mid, h, x, i, False) * g1(w-mid+1, h, i, True)

    store[(w, h, x)] = total
    return total

def g2(w, h, x, y, odd=True):
    # print w, h, x, y
    if w <= 0 or h <= 0:
        raise

    if x > y:
        return g2(w, h, y, x, odd)

    if not odd:
        return int((h+1)**(w-2) - g2(w, h, x, y))

    try:
        return store[(w, h, x, y)]
    except:
        pass

    if w == 1:
        if x != y: return 0
        return 1 if x % 2 else 0
    elif w == 2:
        total = y
        return 1 if total % 2 else 0

    mid = w / 2 + 1

    total = 0
    for i in xrange(h+1):
        if i % 2:
            # i is odd
            total += g2(mid, h, x, i, True) * g2(w-mid+1, h, i, y, True)
            total += g2(mid, h, x, i, False) * g2(w-mid+1, h, i, y, False)
        else:
            total += g2(mid, h, x, i, True) * g2(w-mid+1, h, i, y, False)
            total += g2(mid, h, x, i, False) * g2(w-mid+1, h, i, y, True)

    store[(w, h, x, y)] = total
    # print store
    return total

# import pdb; pdb.set_trace()
# assert g2(1, 1, 0, 1) == 0
# assert g2(1, 1, 1, 1) == 1
# assert g2(1, 1, 1, 1, False) == 0
# assert g2(2, 2, 0, 0) ==  0
# assert g2(2, 2, 0, 1) == 1
# assert g2(3, 2, 0, 0) == 1
# assert g2(3, 2, 0, 0, False) == 2
# assert g2(4, 2, 0, 0) + g2(4, 2, 0, 1) + g2(4, 2, 0, 2) == g1(4, 2, 0)
assert g1(4, 2, 0) + g1(4, 2, 1) + g1(4, 2, 2) == g(4, 2) == g0(4, 2)
# assert g2(4, 2, 0, 1) == 3
# assert g2(4, 2, 0, 1, False) == 5
# assert g1(1, 1, 0) == 0
# assert g1(1, 1, 1) == 1
# assert g1(2, 2, 0) == 1
# assert g1(2, 2, 0, False) == 2
# assert g1(3, 2, 0) == 3
# assert g1(3, 2, 1) == 4
# assert g1(4, 2, 0) == 9
# print  g1(4, 2, 1)
# assert g1(4, 2, 1) == 4
assert F(4, 2) == 10
assert F(13, 10) == 3729050610636
assert F(10, 13) == 37959702514
assert F(100, 100) % 1000000007 == 841913936
