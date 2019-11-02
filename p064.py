import math
import copy

class Number:
    def __init__(self, x, y, c = 1):
        # x + c * sqrt(y)
        self.x = x
        self.y = y
        self.c = c
        assert self.y >= 0
    def less0(self):
        
        if self.x >= 0 and self.c >= 0:
            return False
        if self.x < 0 and self.c < 0:
            return True
        if self.x < 0:
            # c * sqrt(y) < -x
            return self.c * self.c * self.y < self.x * self.x
        if self.c < 0:
            # x < -c * sqrt(y)
            return self.x * self.x < self.c * self.c * self.y
        assert False
    def inverse(self):
        self.x = -self.x
        self.c = -self.c
    def __str__(self):
        if self.y == 0:
            return str(self.x)
        if self.x == 0:
            return "sqrt({})".format(self.y) if self.c == 1 else "{}sqrt({})".format(self.c, self.y)
        if self.c == 1:
            return "({}+sqrt({}))".format(self.x, self.y)
        return "({}+{}sqrt({}))".format(self.x, self.c, self.y)
    def __eq__(self, o):
        if type(o) == int:
            return self.y == 0 and self.x == o 
        return self.x == o.x and ((self.y == o.y and self.c == o.c) or (self.y == 0 and o.y == 0))
    def __imul__(self, o):
        if self.y == 0:
            p = self.x
            self.x = p * o.x
            self.y = o.y
            self.c = p * o.c
            return self

        if o.y == 0:
            self.x = self.x * o.x
            self.c = self.c * o.x
        elif self.x == o.x and self.y == o.y and self.c == -o.c:
            self.x = self.x * self.x - self.c * self.c * self.y
            self.y = 0
        elif self.x == -o.x and self.y == o.y and self.c == o.c:
            self.x = self.c * self.c * self.y - self.x * self.x
            self.y = 0
        else:
            raise Exception("unexpected")
        return self

class Frac:
    def __init__(self, x, y):
        # x / y
        self.x = x
        self.y = y
    def __str__(self):
        if self.x.less0() and self.y.less0():
            self.x.inverse()
            self.y.inverse()
        if self.y == 1:
            return str(self.x)
        return "{}/{}".format(self.x, self.y)
    def __repr__(self):
        return str(self)
    def __eq__(self, o):
        return self.x == o.x and self.y == o.y
    def process(self):
        assert self.y.y == 0
        if self.x.x != 0:
            g = math.gcd(self.x.x, self.y.x)
            g = math.gcd(g, self.x.c)
            self.x.x = int(self.x.x / g)
            self.x.c = int(self.x.c / g)
            self.y.x = int(self.y.x / g)
        # pick >= 1
        #  self.x.x + self.x.c * sqrt(self.x.y) / self.y.x
        minus = 0
        # self.x.x + self.x.c * sqrt(self.x.y) - minus >= self.y.x
        # self.x.c * sqrt(self.x.y) >= self.y.x + minus - self.x.x
        # self.x.c * self.x.c * self.x.y >= (self.y.x + minus - self.x.x) * (self.y.x + minus - self.x.x)
        # 
        while self.x.c * self.x.c * self.x.y >= (self.y.x + minus - self.x.x) * (self.y.x + minus - self.x.x):
            minus += self.y.x
        self.x.x -= minus
        return int(minus / self.y.x)

    def trans(self):
        if self.y.y == 0:
            return
        number = Number(self.y.x, self.y.y, -self.y.c)
        # print('trans number: ' + str(number))
        # print('self.x: ' +str(self.x))
        # print('self.y: ' +str(self.y))
        self.x *= number
        # print('self.x: ' +str(self.x))
        self.y *= number
        # print('self.y: ' +str(self.y))
    def inverse(self):
        self.x, self.y = self.y, self.x

def main(N):
    ans = 0
    for x in range(N):
        y = int(math.sqrt(x))
        if y * y == x:
            continue
        arr = []
        fracArr = []
        number = Number(0, x) # sqrt(x)
        frac = Frac(number, Number(1, 0)) # sqrt(x)
        fracArr.append(copy.deepcopy(frac))
        while True:
            # print("frac: ", frac)
            r = frac.process()
            # print("process: ", frac)
            arr.append(r)
            frac.inverse()
            # print("inverse: ", frac)
            frac.trans()
            # print("trans: ", frac)
            fracArr.append(copy.deepcopy(frac))
            if frac in fracArr[:-1]:
                idx = fracArr.index(frac)
                period = len(fracArr) - idx - 1
                if period % 2 == 1:
                    ans += 1
                break
        # print(arr)
        # print(fracArr)
    print(ans)


if __name__ == "__main__":
    main(14)
    main(10000)
    main(10001)