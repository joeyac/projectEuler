#include<bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include <chrono>
using namespace std::chrono;
#endif

typedef long long ll;
typedef pair<int,int> PI;

int M;
int ans;

void readInput() {

}

void simpleProcess() {
    printf("simpleProcess M=%d\n", M);
    ans = 0;
    for (int i = 1; i <= M; ++i)
        for (int j = i; j <= M; ++j)
            for (int k = j; k <= M; ++k)
            {
                int d = i * i + k * k + j * j + 2 * i * j;
                int ds = sqrt(d);
                if (ds * ds == d) {
                    // printf("(%d+%d)^2+%d^2=%d^2\n", i, j, k, ds);
                    // printf("%d^2+%d^2=%d^2  i=%d, j=%d, k=%d\n", i + j, k, ds, i, j, k);
                    ans++;
                }
            }
    printf("simpleProcess ans=%d\n", ans);
}

void doProcess() {
    // 这个暴力二分竟然也可以过……跑大概50s 233333
    int lowM = 1000, upM = 2000;
    int aim = 1000000;
    int ansM = -1;
    while (lowM <= upM) {
        M = (lowM + upM) / 2;
        simpleProcess();
        if (ans >= aim ) upM = M - 1, ansM = M;
        else lowM = M + 1;
    }
    printf("ansM = %d\n", ansM);
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("data.in", "r", stdin);
#endif

    readInput();

#ifndef ONLINE_JUDGE
auto start = high_resolution_clock::now();
#endif
    doProcess();

#ifndef ONLINE_JUDGE
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Time taken by solution: "
         << duration.count() / 1000000.0 << " seconds" << endl;
#endif
    return 0;
}