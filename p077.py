import math

INF = int(1e6 + 7)

primes = []
isPrime = [True for i in range(INF)]
isPrime[0] = isPrime[1] = False
for i in range(2, INF):
    if isPrime[i]:
        primes.append(i)
        j = i + i
        while j < INF:
            isPrime[j] = False
            j += i

dp = {}
def func(x, y):
    if (x,y) in dp:
        return dp[(x,y)]
    # print(x, y)
    if y == 1 or x == 1:
        return 0
    if y == 2:
        return 1 if x % 2 == 0 else 0
    if x < y:
        dp[(x,y)] = func(x,x)
    elif x == y:
        dp[(x,y)] = 1 if isPrime[x] else 0
        dp[(x,y)] += func(x,y-1)
    else:
        dp[(x,y)] = func(x,y-1)
        if isPrime[y]:
            dp[(x,y)] += func(x-y,y)
    return dp[(x,y)]

for i in range(1, 11):
    print(func(10,i))


for i in range(1, 100):
    if func(i, i) >= 5000:
        print(i, func(i, i))
        break