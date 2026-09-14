# for i in range(1, 800):
#     for j in range(1, 800):
#         for k in range(1, 800):
#             if i + j + k != 1000:
#                 continue
#             if i ** 2 + j ** 2 == k ** 2:
#                 print(i, j, k)
#                 print(i * j * k)
#                 exit()

# more efficient version
import math 

s = 1000
if s % 2 == 1:
    print(None)
    exit()

s2 = s // 2
mlimit = math.isqrt(s2) + 1
for m in range(2, mlimit):
    if s2 % m == 0:
        sm = s2 // m
        while sm % 2 == 0:
            sm //= 2
        if m % 2 == 1:
            k = m + 2
        else:
            k = m + 1
        while k < 2 * m and k <= sm:
            if sm % k == 0 and math.gcd(k, m) == 1:
                d = s2 // (k * m)
                n = k - m
                a = d * (m * m - n * n)
                b = 2 * d * m * n
                c = d * (m * m + n * n)
                print(a, b, c)
            k += 2

'''
if s odd: no solution
half = s / 2
for m in 2 to sqrt(half):
    if m doesn't divide half: skip
    remaining = half / m   # this equals k · d
    strip factors of 2 from remaining  # since k must be odd
    for k in each odd divisor of remaining in range (m, 2m) with gcd(k, m) = 1:
        d = half / (m · k)
        n = k - m
        emit triple (d(m² - n²), 2dmn, d(m² + n²))
'''
