
cnt = 0
for x in range(1, 10):
    y = 1
    while True:
        v = x ** y
        if len(str(v)) == y:
            while len(str(v)) == y:
                print(str(x) + "^" + str(y) + "=" + str(v))
                y += 1
                v = x ** y
                cnt += 1
            break
        y += 1

print(cnt)
# 49