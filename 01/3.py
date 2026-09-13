x = 600851475143

# generate primes fast ;-;
i = 2
factors = []
while i <= x:
    while x % i == 0:
        factors.append(i)
        x //= i
    i += 1
print(factors)
