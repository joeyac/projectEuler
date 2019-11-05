import math
import time
import decimal
decimal.getcontext().prec = 200

def run():
    N = 100
    ans = 0
    for i in range(1, N + 1):
        num = decimal.Decimal(i)
        y = num.sqrt()
        z = int(y)
        if z * z == i:
            continue
        y = str(y).replace('.', '')
        val = sum([int(x) for x in y[:100]])
        ans += val
    print(ans)

def main():
    start = time.time()
    run()
    end = time.time()
    print('use time: ', end - start)

if __name__ == "__main__":
    main()
