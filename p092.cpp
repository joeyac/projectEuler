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

bool solve(int x) {
    int y = 0;
    while (x) {
        int t = x % 10;
        y += t * t;
        x /= 10;
    }
    if (y == 1) return false;
    else if (y == 89) return true;
    else return solve(y);
}

void doProcess() {
    int N = 10000000;
    int cnt[] = {0, 0};
    for (int i = 1; i < N; ++i)
        cnt[solve(i)]++;
    printf("%d %d\n", cnt[0], cnt[1]);
// 1418853 8581146
// Time taken by solution: 0.536569 seconds
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