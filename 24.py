
xs = []
xs.append(1)

for i in range(1, 11):
    xs.append(xs[-1] * i)

def sol(total):
    v = []
    choose = range(0, 10)

    for i in range(10):
        # position
        for j in choose:
            if j in v: continue

            branch = xs[10-i-1]
            if total > branch:
                total -= branch
                continue
            else:
                v.append(j)
                break

    return ''.join(str(k) for k in v)

print sol(1000000)
