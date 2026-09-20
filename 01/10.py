isPrime = [1] * 2000000
isPrime[1] = 0
i = 2
while i * i <= 2000000:
    if isPrime[i]:
        for j in range(i * 2, 2000000, i):
            isPrime[j] = 0
    i += 1
# print(isPrime[:12])

ans = 0
for i in range(2, 2000000):
    if isPrime[i]:
        ans += i
print(ans)
