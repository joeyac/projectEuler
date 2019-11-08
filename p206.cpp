#include<bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include <chrono>
using namespace std::chrono;
#endif

typedef unsigned long long ll;
typedef pair<int,int> PI;

// max_value = 1929394959697989990
// min_value = 1020304050607080900
// L = int(math.sqrt(min_value)) # 1010101010
// R = int(math.sqrt(max_value)) # 1389026623
const ll L = 1010101010L;
const ll R = 1389026623L;

void readInput() {

}

bool check(ll x) {
    x = x * x;
    // 1_2_3_4_5_6_7_8_9_0
    int cnt = 19;
    while (x) {
        if (cnt % 2 == 1 && x % 10 != ((cnt + 1) / 2) % 10) return false;
        x /= 10;
        cnt--;
    }
    assert(cnt == 0);
    return true;
} 

void doProcess() {
    for (ll i = L; i <= R; ++i) {
        if ((i - L) % ((R - L) / 100) == 0) printf("cur: %lld\n", i);
        if (check(i)) {
            printf("ans: %lld\n", i);
            return;
        }
    }
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
         << duration.count() << " microseconds" << endl;
#endif
    return 0;
}