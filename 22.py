A = ord('A')
def score(name):
    return sum([ord(i) - A + 1 for i in name])


with open('p022_names.txt') as ifile:
    data = [k.replace('"','') for k in ifile.read().upper().split(',')]

data.sort()

assert score("COLIN") == 53

# import pdb; pdb.set_trace()
total = 0
for id, i in enumerate(data):
    # print score(i), i
    total += (id+1) * score(i)

print total
