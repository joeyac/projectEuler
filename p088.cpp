#include<bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include <chrono>
using namespace std::chrono;
#endif

typedef long long ll;
typedef pair<int,int> PI;
const int MAXK = 12000;
const int maxn = MAXK * 2 + 1;

int ans[MAXK + 1];

/*
确定n，推k的最小值最大值
n = (a*b)*c*(1...1) = a*b + c + d*1      k1=2+d
  = a*b*c*(1...1)   = a + b + c + e*1    k2=3+e

a,b,c>=2
a*b>=a+b => d<=e => k1 < k2
n为若干素数之积有k_max = n-sum(a_i)+num_of_a_i

k_min显然当n=x*y时
n=x*y*(1...1) = x + y + z*1
x+y>=2sqrt(xy)
k = n - (x + y) + 2 <= n + 2 - 2sqrt(xy)
x,y其中一者为n的最小因子时有k_min

=================================
这样的话可以递归从最小的n开始，找到能map上的所有的k并标记

*/

void readInput() {
}

void updateAns(int n, int sum, int step) {
    // printf("%d %d %d\n", n, sum, step);
    int k = sum + step;
    if (k <= MAXK && ans[k] == -1) ans[k] = n;
}

// solve(n,n,n)
// solve(n,n-x,n/x)
void solve(int n, int sum, int product, int step = 0, int mini = 2) {
    // K=n-sum(a_i)+num_of_a_i
    // printf("%d %d %d %d %d\n", n, sum, product, step, mini);
    if (sum < 0) 
        return;

    if (product == 1)
        return updateAns(n, sum, step);

    if (step >= 1 && sum - product >= 0) {
        updateAns(n, sum - product, step + 1);
    }

    int m = sqrt(n);
    int ret = -1;
    for (int i = mini; i <= m; ++i) {
        if (product % i == 0) {
            solve(n, sum - i, product / i, step + 1, i);
        }
    }
}

void doProcess() {
    memset(ans, -1, sizeof(ans));
    // solve(4,4,4);

    for (int i = 2; i <= maxn; i++) {
        solve(i,i,i);
    }
    set<int> S;
    for (int i = 1; i <= MAXK; i++) {
        if (ans[i] != -1) S.insert(ans[i]);
        // printf("ans[%d]=%d\n", i, ans[i]);
    }
    printf("%d\n", accumulate(S.begin(), S.end(), 0));
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