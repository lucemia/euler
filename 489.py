# n^3 + 3an^2 + 3a^2n + a^3 + b
# 3an^2 + 3a^2n + a^3
# a(3n^2 + 3an + a^2)
# 3*5^2 + 15 + 1
# 75+16 = 91

# 48 + 12 + 1 = 61
# 108 + 18 + 1 = 127
# http://math.stackexchange.com/questions/1032495/maximum-gcd-of-two-polynomials
import sympy

def gcd(f1, f2, n):


# import numpy as np
# SIZEA = 5
# SIZEB = 5
# SOLS = np.zeros((SIZEA, SIZEB), np.int32)
# # COUNTS = np.zeros((SIZEA, SIZEB), np.int32)

# def gcd(a, b):
#     if a > b: a, b = b, a

#     div = b % a
#     if div == 0: return a

#     return gcd(a, div)

# def count(a, b):
#     MAX = 0

#     # fs = []
#     BEST = (a**3) * 7
#     # print BEST

#     for n in xrange(10000):
#         na = n**3 + b
#         nb = (n+a)**3 + b

#         x = gcd(na, nb)
#         if x == BEST:
#             return n
#         # print na, nb, x
#         # fs.append(x)

#     # print fs
#         # if x >= MAX:
#             # MAX = x
#         # else:
#             # print a, b, fs
#             # return n-1


# def sol(a, b):
#     print a, b, '\n', SOLS
#     if SOLS[a-1, b-1]:
#         pass
#     if a == 1 and b == 1:
#         SOLS[a-1, b-1] = count(a, b)
#     else:
#         total = count(a, b)
#         # print a, b, total
#         if a > 1:
#             total += sol(a-1, b)
#         if b > 1:
#             total += sol(a, b-1)
#         if a > 1 and b > 1:
#             total -= sol(a-1, b-1)
#         SOLS[a-1, b-1] = total

#     return SOLS[a-1, b-1]

# assert gcd(5**3+1, 6**3+1) == 7
# # assert count(1, 1) == 5
# print count(5, 5)
# # print count(1,1)
# print count(2, 1)
# assert sol(5, 5) == 128878
# assert sol(10, 10) == 32936544
