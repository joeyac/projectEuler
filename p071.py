import math
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

def main(N):
    aim = Frac(3, 7)
    ans = Frac(0, 1)
    for d in range(2, N):
        if N > 100 and d % (N // 100) == 0:
            print('d =', d)
        i = int(d * 3 / 7)
        while i >= 1:
            g = math.gcd(i, d)
            cur = Frac(i, d)
            if cur == aim or g != 1:
                i -= 1
                continue
            if cur > ans:
                ans = cur
            break
    print(ans)

if __name__ == "__main__":
    # main(8 + 1)
    main(1000000 + 1)