import math
import time

def arr1(x):
    return x * (3 * x - 1) // 2

def arr2(x):
    return x * (3 * x + 1) // 2

def arr(x):
    return [arr1(x), arr2(x)]

def run():
    N = 100000
    mod = 1000000
    ans = [1]
    for i in range(1, N + 1):
        ans.append(0)
        k = 1
        while True:
            coeff = (-1) ** (k + 1)
            flag = True
            for t in arr(k):
                if (i - t) >= 0:
                    ans[i] += coeff * ans[i - t] % mod
                else:
                    flag = False
            if flag:
                k += 1
            else:
                break
        ans[i] %= mod
        if ans[i] % mod == 0:
            print(i, ans[i])
            break


def main():
    start = time.time()
    run()
    end = time.time()
    print('use time: ', end - start)

if __name__ == "__main__":
    main()