import os

data = []

with open('data/p059_cipher.txt') as f:
    for line in f.readlines():
        data.extend(map(int, filter(None, line.split(','))))
    q = {}
    for i in data:
        if i in q:
            q[i] += 1
        else:
            q[i] = 1
    ans = [(q[k], k) for k in q]
    ans = sorted(ans)
    print(ans[-5:])
    print(len(data))

def isValid(x):
    if ord('A') <= x <= ord('Z'):
        return True
    if ord('a') <= x <= ord('z'):
        return True
    if ord('0') <= x <= ord('9'):
        return True
    try:
        x = chr(x)
    except Exception as e:
        print(str(e) + " " + x)
        return False
    if x in """ ,./<>?;':"[]{}\\|-_+=!()""":
        return True
    return False

def solve(x, y, z):
    code = [x, y, z]
    n = len(data)
    sd = 0
    cnt = 0
    for i in range(n):
        ori = data[i] ^ code[i % 3]
        sd += ori
        if isValid(ori):
            cnt += 1
    return cnt, sd

def encode(keyList):
    n = len(data)
    oriList = [data[i] ^ keyList[i % 3] for i in range(n)]
    oriList = [chr(item) for item in oriList]
    print("\n=====\n" + ''.join(oriList) + "\n====\n")

def main():
    # print(data)
    mcnt = 0
    ans = 0
    keyList = []
    chs = list(range(ord('a'), ord('z') + 1))
    for a in chs:
        for b in chs:
            for c in chs:
                r1, r2 = solve(a, b, c)
                if r1 > mcnt:
                    mcnt = r1
                    ans = r2
                    keyList = [a, b, c]
    print(mcnt, ans)
    encode(keyList)

if __name__ == "__main__":

    guess = [
        ['e', 'x', 'p']
    ]
    for keyList in guess:
        number = [ord(item) for item in keyList]
        encode(number)
    main()