MX = 1000000
prime = [1] * MX
prime[0] = prime[1] = 0
for i in range(2, MX):
    if prime[i]:
        for j in range(i * 2, MX, i):
            prime[j] = 0
# print(prime[:100])
c = 0
for i in range(MX):
    if prime[i]:
        c += 1
        if c == 10001:
            print(i)
            break
