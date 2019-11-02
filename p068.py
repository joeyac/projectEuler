import itertools

arr = [i + 1 for i in range(10)]
chs = [
    [0, 5, 6],
    [1, 6, 7],
    [2, 7, 8],
    [3, 8, 9],
    [4, 9, 5],
]
ans = ''.join(map(str, [0 for i in range(16)]))
for cur in itertools.permutations(arr):
    if 10 not in cur[:5]:
        continue
    cur_arr = []
    sum_arr = []
    for ix in chs:
        cur_arr.append([cur[k] for k in ix])
        sum_arr.append(sum(cur_arr[-1]))
    if not all([i == sum_arr[0] for i in sum_arr]):
        continue
    mink = -1
    minv = 11
    for i in range(len(cur_arr)):
        if cur_arr[i][0] < minv:
            mink = i
            minv = cur_arr[i][0]
    cur_arr = cur_arr[mink:] + cur_arr[:mink]
    cur_ans = ''
    for a in cur_arr:
        for k in a:
            cur_ans += str(k)
    ans = max(ans, cur_ans)
print(ans)
