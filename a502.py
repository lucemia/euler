# -*- encoding=utf8 -*-

store = {}

def g(w, h, odd=True):
    # print w, h
    if w <= 0 or h <= 0:
        if odd: return 0
        return 1

    if not odd:
        return (h+1)**w - g(w, h)

    if (w, h) in store:
        # print store
        return store[(w, h)]

    # 按照第一個 0 的位置進行 dp
    total = 0
    # 第一欄是 0
    total = g(w-1, h)
    for i in range(w):
        total += g(i+1, h-1, False) * g(w-i-2, h, False)
        total += g(i+1, h-1, True) * g(w-i-2, h, True)

    ## 全部都不是0 的有隱含在內了

    store[(w,h)] = total
    return total

def F(w, h):
    return g(w, h-1) - g(w, h-2)


if __name__ == '__main__':
    assert F(4, 2) == 10
    assert F(13, 10) == 3729050610636
    assert F(10, 13) == 37959702514
    assert F(100, 100) % 1000000007 == 841913936

# print F(10000, 10000)
# print (F(10**12,100) + F(10000,10000) + F(100,10**12)) % 1000000007
# for x in range(2, 10):
#     for y in range(2, 10):
#         print x, y, F(x, y)

# 我目前的進展有點類似: F(w, h) = G(w, h-1) (G 拿掉了條件 4, 變成block要基數個)
# G(w, h-1) = g(w, h-1) - g(w, h-2) (g 拿掉了條件 5, 變成只要 <= h)
# 計算 g(w, h) 過程理論上可以用 dp(還沒細想) ... 由於最後要算 F(10**12,100), F(100, 10**12) dp 可能要弄成 w, h 雙向都能化簡才有機會...
