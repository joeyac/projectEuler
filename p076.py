import math
# https://brilliant.org/wiki/partition-of-an-integer/
# https://math.stackexchange.com/questions/2675382/calculating-integer-partitions

def arr(x):
    return x * (3 * x  - 1) // 2

N = 100
ans = [1]
for i in range(1, N + 1):
    ans.append(0)
    for k in range(1, i + 1):
        coeff = (-1) ** (k + 1)
        for t in [arr(k), arr(-k)]:
            if (i - t) >= 0:
                ans[i] += coeff * ans[i - t]

for i in range(1, 6 + 1):
    print(ans[i] - 1)
print(ans[100] - 1)
