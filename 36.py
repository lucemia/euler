
def is_palindromes(n):
    return n == int(''.join(reversed(bin(n)[2:])), 2) and n == int(''.join(reversed(str(n))))

assert is_palindromes(585)

total = 0
for i in range(1000000):
    if is_palindromes(i):
        total += i

print total
