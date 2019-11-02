
def Triangle(x):
    return x * (x + 1) / 2

def Square(x):
    return x * x

def Pentagonal(x):
    return x * (3 * x - 1) / 2

def Hexagonal(x):
    return x * (2 * x - 1)

def Heptagonal(x):
    return x * (5 * x - 3) / 2

def Octagonal(x):
    return x * (3 * x - 2)

def main(N = 3):
    fuc_list = [Triangle, Square, Pentagonal, Hexagonal, Heptagonal, Octagonal]
    fuc_list = fuc_list[:N]
    data = {i : set() for i in range(N)}
    for i in range(N):
        fuc = fuc_list[i]
        x = 1
        while True:
            v = int(fuc(x))
            if 1000 <= v <= 9999:
                data[i].add(str(v))
            if v >= 10000:
                break
            x += 1
    for k in data:
        print(k, data[k])
    
    curList = [-1 for i in range(N)]
    used = [False for i in range(N)]
    def dfs(x):
        if x == N:
            # print("DEBUG:", curList)
            if curList[-1][2:] == curList[0][:2]:
                print(curList, sum([int(i) for i in curList]))
            return
        if x == 0:
            chid = 0
            used[chid] = True
            for d in data[chid]:
                curList[x] = d
                dfs(x + 1)
            used[chid] = False
        else:
            for k in data:
                if used[k]:
                    continue
                used[k] = True
                for d in data[k]:
                    if curList[x - 1][2:] == d[:2]:
                        curList[x] = d
                        dfs(x + 1)
                used[k] = False
    print('start process')
    dfs(0)

if __name__ == "__main__":
    # ['8256', '5625', '2512', '1281', '8128', '2882'] 28684
    main(6)
