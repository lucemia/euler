
def is_Pandigital(n):
    i = 1
    m = ""
    while True:
        m += str(n*i)
        if '0' in m:
            return False

        if len(m) > 9:
            return False

        if len(set(m)) < len(m):
            return False

        if len(m) == 9:
            return m

        i += 1

assert is_Pandigital(9)
assert is_Pandigital(192)
assert not is_Pandigital(4)

for i in range(91, 98):
    if is_Pandigital(i):
        print i

for i in range(900, 1000):
    if is_Pandigital(i):
        print i


for i in range(9000, 10000):
    v = is_Pandigital(i)
    if v:
        print i, v
