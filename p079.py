import math
import time
import os
from collections import defaultdict

with open(os.path.join('data', 'p079_keylog.txt')) as f:
    data = list(filter(None, f.read().split('\n')))
    data = sorted(list(set(data)))
    print(data)
    print(len(data))

# '129', '160', '162', '168', '180', '289'
# 1 6 2 8 9 0
# '290', '316', '318', '319', '362', '368', '380', '389', '620',
# '629', '680', '689', '690', '710', '716', '718', '719', '720',
# '728', '729', '731', '736', '760', '762', '769', '790', '890'
# 7 3 1 6 2 8 9 0
# 头铁随手推出来的……正解应该不是手推吧……妈耶真的是手推……


def check(x):
    v = str(x)
    all_ok = True
    for k in data:
        st = 0
        ok = True
        for i in range(3):
            if k[i] in v[st:]:
                idx = v[st:].index(k[i])
                st += idx + 1
            else:
                ok = False
                break
        if not ok:
            all_ok = False
            break
    if all_ok:
        print('ans=', x)

def run():
    count = [defaultdict(int) for i in range(3)]
    for d in data:
        for i in range(3):
            count[i][d[i]] += 1
    print(count)
    check(73162890)

def main():
    start = time.time()
    run()
    end = time.time()
    print('use time: ', end - start)

if __name__ == "__main__":
    main()
