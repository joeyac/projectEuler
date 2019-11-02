import math

class Frac:
    def __init__(self, x, y):
        # x / y
        self.x = x
        self.y = y
    def __str__(self):
        if self.x < 0 and self.y < 0:
            self.x = -self.x
            self.y = -self.y
        if self.y == 1:
            return str(self.x)
        if self.y == -1:
            return str(-self.x)
        g = math.gcd(self.x, self.y)
        self.x = self.x // g
        self.y = self.y // g
        return "{}/{}".format(self.x, self.y)
    def __repr__(self):
        return str(self)
    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

def arrE(st, n, reverse = False):
    idx = n - 1 if reverse else st
    while True:
        if idx >= n or (reverse and idx < st):
            break
        if idx == 0:
            yield 2
        else:
            if idx % 3 == 2:
                yield (idx + 1) // 3 * 2
            else:
                yield 1
        idx += -1 if reverse else 1

def main(N):
    frac = Frac(0, 1)
    for i in arrE(1, N, True):
        frac.x += frac.y * i
        frac.x, frac.y = frac.y, frac.x
    frac.x += 2 * frac.y
    print(frac)
    print(sum([int(i) for i in str(frac.x)]))

if __name__ == "__main__":
    main(10)
    main(100)
