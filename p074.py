INF = 1000000

fac = [1 for i in range(10)]
for i in range(1, 10):
    fac[i] = fac[i - 1] * i

def get(x):
    y = str(x)
    ret = 0
    for b in y:
        ret += fac[int(b)]
    return ret

maxu = -1
ans = 0
for i in range(INF):
    if i % (INF // 100) == 0:
        print('process ', i)
    arr = [i]
    while True:
        cur = get(arr[-1])
        if cur in arr:
            idx = len(arr)
            maxu = max(maxu, idx)
            if idx == 60:
                ans += 1
            break
        arr.append(cur)
    
print(maxu, ans)