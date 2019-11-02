import math


# INF = int(1e5 + 9)
# phi = [i for i in range(INF)]
# for i in range(2, INF):
#     if phi[i] == i:
#         j = i
#         while j < INF:
#             phi[j] = phi[j] // i * (i - 1)
#             j += i

class Frac:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        g = math.gcd(self.x, self.y)
        self.x = self.x // g
        self.y = self.y // g
        return '{}/{}'.format(str(self.x), str(self.y))
    def __repr__(self):
        return str(self)
    def __eq__(self, o):
        str(self)
        str(o)
        return self.x == o.x and self.y == o.y
    def __lt__(self, o):
        ct = (self.y < 0) + (o.y < 0)
        return self.x * o.y > o.x * self.y if ct == 1 else self.x * o.y < o.x * self.y

    def __gt__(self, o):
        ct = (self.y < 0) + (o.y < 0)
        return self.x * o.y < o.x * self.y if ct == 1 else self.x * o.y > o.x * self.y

def main(N, x, y):
    aim = Frac(x, y)
    ans = Frac(0, 1)
    ret = 0
    for d in range(2, N):
        if N > 100 and d % (N // 100) == 0:
            print('d =', d)
        i = int(d * x / y)
        while i >= 1:
            g = math.gcd(i, d)
            cur = Frac(i, d)
            if cur == aim or g != 1:
                i -= 1
                continue
            ret += 1
            # print(cur)
            if cur > ans:
                ans = cur
            # break
            i -= 1
    print(ans, ret)
    return ret

if __name__ == "__main__":
    a1 = main(8 + 1, 1, 2)
    a2 = main(8 + 1, 1, 3)
    r1 = main(12000 + 1, 1, 2)
    r2 = main(12000 + 1, 1, 3)
    print(a1 - a2 - 1, r1 - r2 - 1)
