#include<bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include <chrono>
using namespace std::chrono;
#endif

typedef long long ll;
typedef pair<int,int> PI;

const int maxn = 1e6 + 7;
const int maxm = 5e7;
// const int maxm = 50;
bool flag[maxm];
bool isP[maxn];
int primes[maxn], cnt = 0;

void readInput() {
    fill(isP, isP + maxn, true);
    memset(flag, false, sizeof(flag));
    isP[0] = isP[1] = false;
    for (int i = 2; i < maxn; ++i)
    {
        if (isP[i])
        {
            primes[cnt++] = i;
            for (int j = i; j < maxn; j += i)
                isP[j] = false;
        }
    }
}

ll f(ll x, ll y) {
    ll ret = 1;
    while (y) {
        if (y & 1) ret *= x;
        x *= x;
        y >>= 1;
    }
    return ret;
}

void doProcess() {
    for (int i = 0; i < cnt && f(primes[i], 4) < maxm; ++i)
        for (int j = 0; j < cnt && f(primes[i], 4)+f(primes[j], 3) < maxm; ++j)
            for (int k = 0; k < cnt && f(primes[i], 4)+f(primes[j], 3)+f(primes[k], 2) < maxm; ++k)
                flag[f(primes[i], 4)+f(primes[j], 3)+f(primes[k], 2)] = true;
    int ans = 0;
    for (int i = 0; i < maxm; ++i)
        if (flag[i]) ++ans;

    vector<int> test = {28,33,49,47};
    for (auto x: test)
        printf("%d\n", flag[x]);
    printf("ans=%d\n", ans);

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