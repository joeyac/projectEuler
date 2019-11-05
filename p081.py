import os
import math
import time
import decimal
decimal.getcontext().prec = 200
INF = int(1e9 + 7)

with open(os.path.join('data', 'p081_matrix.txt')) as f:
    dataList = list(filter(None, f.read().split('\n')))
    data = []
    for item in dataList:
        data.append(
            list(map(int, filter(None, item.split(','))))
        )
print(len(data))
print(len(data[0]))
N = len(data)
M = len(data[0])

def run():
    dp = [[INF for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                dp[i][j] = data[i][j]
            else:
                if i > 0:
                    dp[i][j] = min(dp[i-1][j] + data[i][j], dp[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j-1] + data[i][j], dp[i][j])
    print(dp[N-1][M-1])

def main():
    start = time.time()
    run()
    end = time.time()
    print('use time: ', end - start)

if __name__ == "__main__":
    main()
