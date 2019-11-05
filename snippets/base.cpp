#include<bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include <chrono>
using namespace std::chrono;
#endif

void readInput() {

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