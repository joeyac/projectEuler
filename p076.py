import math

def arr1(x):
    return x * (3 * x - 1) // 2

def arr2(x):
    return x * (3 * x + 1) // 2

def arr(x):
    return [arr1(x), arr1(-x)]
    # equal:
    # return [arr1(x), arr2(x)]

N = 100
ans = [1]
for i in range(1, N + 1):
    ans.append(0)
    for k in range(1, i + 1):
        coeff = (-1) ** (k + 1)
        for t in arr(k):
            if (i - t) >= 0:
                ans[i] += coeff * ans[i - t]
            else:
                break

for i in range(1, 6 + 1):
    print(ans[i] - 1)
print(ans[100] - 1)


dp = {}
def func(x, y):
    if (x,y) in dp:
        return dp[(x,y)]
    if x == 1 or y == 1:
        return 1
    if x < y:
        dp[(x,y)] = func(x, x)
    elif x == y:
        dp[(x,y)] = func(x, x - 1) + 1
    else:
        dp[(x,y)] = func(x - y, y) + func(x, y - 1)
    return dp[(x,y)]
print(func(100, 100) - 1)