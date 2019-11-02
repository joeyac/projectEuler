
INF = int(1e7 + 9)
phi = [i for i in range(INF)]
for i in range(2, INF):
    if phi[i] == i:
        j = i
        while j < INF:
            phi[j] = phi[j] // i * (i - 1)
            j += i

print(phi[87109])
ratio = INF
ans = -1
for i in range(2, int(1e7 + 1)):
    s1 = str(i)
    s2 = str(phi[i])
    if sorted(s1) == sorted(s2):
        if i / phi[i] < ratio:
            ratio = i / phi[i]
            ans = i
            print('i=', i)

print("ans=", ans, "ratio", ratio)

# 79180
# i= 21 
# i= 291
# i= 2817
# i= 2991
# i= 4435
# i= 20617
# i= 45421
# i= 69271
# i= 75841
# i= 162619
# i= 176569
# i= 284029
# i= 400399
# i= 474883
# i= 732031
# i= 778669
# i= 783169
# i= 1014109
# i= 1288663
# i= 1504051
# i= 1514419
# i= 1924891
# i= 1956103
# i= 2006737
# i= 2044501
# i= 2094901
# i= 2239261
# i= 2710627
# i= 2868469
# i= 3582907
# i= 3689251
# i= 4198273
# i= 4696009
# i= 5050429
# i= 5380657
# i= 5886817
# i= 6018163
# i= 6636841
# i= 7026037
# i= 7357291
# i= 7507321
# i= 8316907
# i= 8319823
# ans= 8319823 ratio 1.0007090511248113