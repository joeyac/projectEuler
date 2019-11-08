#include<bits/stdc++.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include <chrono>
using namespace std::chrono;
#endif

typedef long long ll;
typedef pair<int,int> PI;
/*
这道题和前面一道德州扑克的题是我做过最恶心的题……mmp怎么能有这么恶心的模拟啊
GO	 A1	 CC1 A2  T1	 R1	 B1	 CH1 B2	 B3
JAIL C1  U1  C2  C3  R2  D1  CC2 D2  D3
FP   E1  CH2 E2  E3  R3  F1  F2  U2  F3
G2J  G1  G2  CC3 G3  R4  CH3 H1  T2  H2 
*/
const int DICE_NUM = 4;
const int DICE_STEP = DICE_NUM * 2;

const int SQUARE_NUM = 40;

const int JAIL_IDX = 10;
const int C1_IDX = 11;
const int E3_IDX = 24;
const int H2_IDX = 39;
const int R1_IDX = 5;
const int G2J_IDX = 30;

const int R_IDX[] = {5, 15, 25, 35};
const int U_IDX[] = {12, 28};

const int CC_IDX[] = {2, 17, 33};
const int CH_IDX[] = {7, 22, 36};

double dice_frac[DICE_STEP + 1];
int N;
PI cnt[SQUARE_NUM];
void readInput() {
    // for (int i = 1; i <= DICE_NUM; ++i)
    // {
    //     for (int j = 1; j <= DICE_NUM; ++j)
    //     {
    //         dice_frac[i+j] += 1.0 / DICE_NUM * 1.0 / DICE_NUM;
    //     }
    // }
    // for (int i = 1; i <= DICE_STEP; ++i)
    //     printf("%d=%.4f\n", i, dice_frac[i]);
    cin >> N;
    // N = 100;
    for (int i = 0; i < SQUARE_NUM; ++i)
        cnt[i].first = 0, cnt[i].second = i;
    srand(time(0));
}

int findNxtR(int idx) {
    int i = 0;
    for (; i < 4; ++i)
        if (R_IDX[i] > idx) break;
    i = i % 4;
    return R_IDX[i];
}

int findNxtU(int idx) {
    int i = 0;
    for (; i < 2; ++i)
        if (U_IDX[i] > idx) break;
    i = i % 2;
    return U_IDX[i];
}

bool isCH(int idx) {
    for (int i = 0; i < 3; ++i)
        if (idx == CH_IDX[i]) return true;
    return false;
}

bool isCC(int idx) {
    for (int i = 0; i < 3; ++i)
        if (idx == CC_IDX[i]) return true;
    return false;
}

int processCH(int idx) {
    assert(isCH(idx));
    static int chidx = -1;
    switch (chidx = (chidx + 1) % 16)
    {
    case 0:
        return 0;
    case 1:
        return JAIL_IDX;
    case 2:
        return C1_IDX;
    case 3:
        return E3_IDX;
    case 4:
        return H2_IDX;
    case 5:
        return R1_IDX;
    case 6:
        return findNxtR(idx);
    case 7:
        return findNxtR(idx);
    case 8:
        return findNxtU(idx);
    case 9:
        return idx - 3;
    default:
        return idx;
    }
}

int processCC(int idx) {
    assert(isCC(idx));
    static int ccidx = 0;
    switch (ccidx = (ccidx + 1) % 16)
    {
    case 0:
        return 0;
    case 1:
        return JAIL_IDX;
    default:
        return idx;
    }
}

void doProcess() {
    int cur = 0;
    cnt[cur].first--;
    int doubleCnt = 0;
    for (int _ = 0; _ < N; ++_)
    {
        // printf("cur=%d\n", cur);
        int t1 = rand() % DICE_NUM + 1, t2 = rand() % DICE_NUM + 1;
        cur += t1 + t2;
        if (t1 + t2 == 2) doubleCnt++;
        else doubleCnt = 0;
        if (doubleCnt >= 3) cur = JAIL_IDX;
        cur = (cur % SQUARE_NUM + SQUARE_NUM) % SQUARE_NUM;
        if (isCC(cur)) cur = processCC(cur);
        else if (isCH(cur)) cur = processCH(cur);
        cur = (cur % SQUARE_NUM + SQUARE_NUM) % SQUARE_NUM;
        if (cur == G2J_IDX) cur = JAIL_IDX;
        cnt[cur].first--;
    }
    int ccc[] = {10, 24, 0};
    for (int j = 0; j < 3; ++j) {
        int i = ccc[j];
        printf("%d=%d,%.2f\n", cnt[i].second, -cnt[i].first, -cnt[i].first * 1.0 / N * 100);
    }
    sort(cnt, cnt + SQUARE_NUM);
    for (int i = 0; i < 3; ++i)
        printf("%d=%d,%.2f\n", cnt[i].second, -cnt[i].first, -cnt[i].first * 1.0 / N * 100);
}

int main() {
#ifndef ONLINE_JUDGE
    // freopen("data.in", "r", stdin);
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
         << duration.count() / 1000000.0 << "seconds" << endl;
#endif
    return 0;
}