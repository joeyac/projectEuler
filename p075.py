import math
INF = 1500000
# a+b+c <= INF
cnt = [0 for i in range(INF)]
N = int(math.sqrt(INF / 2))
print(N)

# assume m>n
# a=m^2-n^2
# b=2mn
# c=m^2+n^2
# https://en.wikipedia.org/wiki/Pythagorean_triple
for m in range(2, N + 1):
    for n in range(1, m):
        if m % 2 == 0 and n % 2 == 0:
            continue
        if m % 2 == 1 and n % 2 == 1:
            continue
        if math.gcd(n, m) != 1:
            continue
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        sumL = a + b + c
        curL = a + b + c
        while curL <= INF:
            cnt[curL - 1] += 1
            curL += sumL

ans = 0
for i in cnt:
    if i == 1:
        ans += 1

print(ans)