
def nx(l):
    for i in range(10**(l-1), 10**l):
        yield i

def find(na, nb):
    for a in nx(na):
        for b in nx(nb):
            c = a*b
            k = str(a) + str(b) + str(c)
            if '0' in k: continue
            if len(k) == 9 and len(set(k)) == 9:
                yield c

# print sum(find(2,3 ))
assert 7254 in set(find(2, 3))

# for i in range(1, 5):
#     for j in range(i, 5):
#         print i, j, len(list(find(i, j)))

print sum(set(find(1, 4)).union(find(2,3)))
# print set(find(3, 3))
