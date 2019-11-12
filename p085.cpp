#include<bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include <chrono>
using namespace std::chrono;
#endif

typedef long long ll;
typedef pair<int,int> PI;

void readInput() {

}

ll get(ll n, ll m) {
    return n * (n + 1) * m * (m + 1) / 4;
}

void doProcess() {
    ll aim = 2e6;
    ll ans = -1, mindiff = 1e18;
    int UPP = 4000;
    for (int n = 1; n <= UPP; ++n) {
        int lowm = 1, upm = UPP;
        while (lowm <= upm) {
            int m = (lowm + upm) / 2;
            if (get(n, m) > aim) upm = m - 1;
            else lowm = m + 1;
        }
        for (int m = lowm - 10; m <= lowm + 10; ++m) {
            ll cur = get(n, m);
            if (abs(aim - cur) < mindiff) {
                mindiff = abs(aim - cur);
                ans = n * m;
                printf("update with %d,%d, mindiff=%lld\n", n, m, mindiff);
            }
        }
    }
    printf("%lld\n", ans);
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