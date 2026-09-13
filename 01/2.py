a = [1, 2, 3]
while a[-1] + a[-2] < 4_000_000:
    a.append(a[-1] + a[-2])
# print(a)
ans = 0
for x in a:
    if x % 2 == 0:
        ans += x
print(ans)
