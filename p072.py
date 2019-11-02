
INF = int(1e7 + 9)
phi = [i for i in range(INF)]
for i in range(2, INF):
    if phi[i] == i:
        j = i
        while j < INF:
            phi[j] = phi[j] // i * (i - 1)
            j += i

sum(phi[2:9])
sum(phi[2:1000001])