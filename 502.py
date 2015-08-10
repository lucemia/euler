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

    assert F(1,1) ==0
    assert F(2,2)==3
    assert F(3,3)==3
    assert F(4,4)==117
    assert F(5,5)==906
    assert F(6,6)==16126
    assert F(7,7)==267803
    assert F(8,8)== 5514147
    assert F(9,9)== 126420564
    assert F(10,10)% 1000000007==256122351
    assert F(100,100)% 1000000007==841913936
    assert F(1000,1000)% 1000000007==270400555

    # F(10000,10000)=7*******7
    # F(100000,100000)=671136691

    # F(1000000,100)=879041470
    # F(10000000,100)=944636434
    # F(100000000,100)=44742678
    # F(1000000000,100)=235563484
    # F(10000000000,100)=284983235
    # F(100000000000,100)=687194943

    # F(100,1000000)=390328558
    # F(100,10000000)=834657901
    # F(100,100000000)=146922709
    # F(100,1000000000)=54039200
    # F(100,10000000000)=541054678
    # F(100,100000000000)=640040539

# print F(10000, 10000)
# print (F(10**12,100) + F(10000,10000) + F(100,10**12)) % 1000000007
# for x in range(2, 10):
#     for y in range(2, 10):
#         print x, y, F(x, y)

# 我目前的進展有點類似: F(w, h) = G(w, h-1) (G 拿掉了條件 4, 變成block要基數個)
# G(w, h-1) = g(w, h-1) - g(w, h-2) (g 拿掉了條件 5, 變成只要 <= h)
# 計算 g(w, h) 過程理論上可以用 dp(還沒細想) ... 由於最後要算 F(10**12,100), F(100, 10**12) dp 可能要弄成 w, h 雙向都能化簡才有機會...

# http://eulersolutions.fr.yuku.com/topic/353/Problem-502#.Vb5DapOqqko
# @mub: for a quick introduction you can look at http://mathcircle.berkeley.edu/BMC6/ps/linear.pdf. For more detailed treatment you can read " Combinatorial Reasoning: An Introduction to the Art of Counting" by Duane DeTemple. An, of course, you should be familiar with dynamic programming and matrix exponentiation)

# It is a really hard problem. Even if you'll grasp all the recurrence-related things it still will be a pretty hard.
# One of possible ways to solve it is:
# 1) generate sample consecutive values of F(m,n) by using bruteforce/backtracking/etc.
# 2) derive 2D recurrence for F(m,n).
# 3) derive 1D recurrences for F(x,n) and F(m,x), where x is fixed.

# When you'll obtain recurrences for F(x,n) or F(m,x) (first one is easier to get), you'll need inital values for it. Use DP for 2D recurrence F(m,n).

# It is only one of ways. There might be other ones.
# I've used characterisitc polynomial approach (Berlekamp-Massey wizardy) for deriving recurrences. Nothing's special. I'd said it is a common way of solving for a bunch of PE problems which involve recurrences. E.g.. 490 is solved by the same approach. Equivalently it can be accomplished by generating functions.
# I hope it will not spoil the problem. Correct me if I'm wrong.


# @mub: characteristic polynomials, generating functions and other recurrence-related combinatorial stuff...

