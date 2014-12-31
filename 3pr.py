
def prime_factor(n):
    for i in xrange(2, n/2):
        if n % i == 0:
            n /= i
            while n % i == 0:
                n /= i

            return [i] + prime_factor(n)

    return [n]

def max_factor(n):
    factors = prime_factor(n)
    return max(factors)


assert max_factor(13195) == 29
print max_factor(600851475143)
