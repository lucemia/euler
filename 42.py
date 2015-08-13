def v(word):
    total = 0
    for i in word:
        total += ord(i) - ord("A") + 1

    return total

x = set()

for i in xrange(10000):
    x.add(i*(i+1) / 2)

# print x
def is_f(word):
    return v(word) in x

assert v("SKY") == 55
assert is_f("SKY")

with open('p042_words.txt') as ifile:
    words = ifile.read().replace('"', '').split(',')
    print len([k for k in words if is_f(k)])
