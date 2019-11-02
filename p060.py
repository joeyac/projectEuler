INF = int(1e4 + 7)
isP = [True for i in range(INF)]
isP[0] = isP[1] = False
primes = []
cnt = 0
for i in range(INF):
    if isP[i]:
        primes.append(i)
        j = 2
        while i * j < INF:
            isP[i * j] = False
            j += 1

def isPrime(x):
    global isP
    x = int(x)
    if x < INF:
        return isP[x]
    y = 2
    while y * y <= x:
        if x % y == 0:
            return False
        y += 1
    return True

invalidSet = set()
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        v1 = str(primes[i]) + str(primes[j])
        v2 = str(primes[j]) + str(primes[i])
        if not isPrime(v1) or not isPrime(v2):
            invalidSet.add((primes[i], primes[j]))

N = 5
arr = [-1 for i in range(N)]
minsum = INF * INF

def check():
    global arr, minsum
    if sum(arr) < minsum:
        print("sum(arr)=" + str(sum(arr)))
        print(arr)
    minsum = min(minsum, sum(arr))
    # if minsum in [535, 792]:
    #     print(arr)
    #     exit(0)

def sol(idx, pre):
    global primes, arr
    if idx == N:
        check()
        return
    for i in range(pre + 1, len(primes)):
        flag = True
        for j in range(0, idx):
            if (arr[j], primes[i]) in invalidSet:
                flag = False
                break
        if flag:
            arr[idx] = primes[i]
            sol(idx + 1, i)

def main():
    print('start sol')
    sol(0, -1)
    print('minsum=' + str(minsum))

if __name__ == "__main__":
# [13, 5197, 5701, 6733, 8389]
# minsum=26033
    for i in range(10):
        print(primes[i])
    main()
