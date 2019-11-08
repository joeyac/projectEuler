#include<bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include <chrono>
using namespace std::chrono;
#endif

typedef pair<int, int> PI;
const int INF = 1e9 + 7;

vector<vector<int> > mat;
vector<vector<int> > ans;
int n, m;

void readInput() {
    ifstream ios("data/p083_matrix.txt");
    string s;
    m = -1;
    while (ios >> s) {
        stringstream ss(s);
        string token;
        int num;
        mat.emplace_back();
        ans.emplace_back();
        auto &curLine = mat.back();
        while (getline(ss, token, ',')) {
            stringstream sss(token);
            sss >> num;
            curLine.push_back(num);
        }
        assert(m == -1 || curLine.size() == m);
        m = curLine.size();
        ans.back().resize(m, INF);
    }
    n = mat.size();
    cout << "n=" << n << " m=" << m << endl;
}

int idx(int x, int y) {
    return x * m + y;
}

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

void doProcess() {
    priority_queue<PI, vector<PI>, greater<PI> > queue;
    // for (int i = 0; i < n; ++i) {
    //     ans[i][0] = mat[i][0];
    //     queue.emplace(ans[i][0], idx(i, 0));
    // }
    ans[0][0] = mat[0][0];
    queue.emplace(ans[0][0], idx(0, 0));
    while (!queue.empty()) {
        auto top = queue.top(); queue.pop();
        int x = top.second / m, y = top.second % m, d = top.first;
        for (int i = 0; i < 4; ++i) {
            int tx = x + dx[i], ty = y + dy[i];
            if (tx < 0 || ty < 0 || tx >= n || ty >= m) continue;
            int dx = d + mat[tx][ty];
            if (dx < ans[tx][ty]) {
                ans[tx][ty] = dx;
                queue.emplace(ans[tx][ty], idx(tx, ty));
            }
        }
    }
    cout << "ans=" << ans[n-1][m-1] << endl;
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