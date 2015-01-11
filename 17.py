from num2words import num2words


def exam(n):
    return len(num2words(n).replace('-', '').replace(' ',''))

assert exam(342) == 23
assert exam(115) == 20

total = 0
for i in xrange(1, 1001):
    total += exam(i)

print total
