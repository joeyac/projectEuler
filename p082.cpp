#include<bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include <chrono>
using namespace std::chrono;
#endif

vector<vector<int> > mat;
int n, m;

void readInput() {
    ifstream ios("data/p082_matrix.txt");
    string s;
    m = -1;
    while (ios >> s) {
        stringstream ss(s);
        string token;
        int num;
        mat.emplace_back();
        auto &curLine = mat.back();
        while (getline(ss, token, ',')) {
            stringstream sss(token);
            sss >> num;
            curLine.push_back(num);
        }
        assert(m == -1 || curLine.size() == m);
        m = curLine.size();
    }
    n = mat.size();
    cout << "n=" << n << " m=" << m << endl;
}

void doProcess() {
    
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("data.in", "r", stdin);
    auto start = high_resolution_clock::now();
#endif

    readInput();
    doProcess();

#ifndef ONLINE_JUDGE
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Time taken by solution: "
         << duration.count() << " microseconds" << endl;
#endif
    return 0;
}