
def main(N, n):
    data = {}
    for i in range(1, n):
        v = i ** 3
        vs = ''.join(sorted(str(v)))
        if vs not in data:
            data[vs] = []
        data[vs].append(v)
        if len(data[vs]) == N:
            print(data[vs])

if __name__ == "__main__":
    # [127035954683, 352045367981, 373559126408, 569310543872, 589323567104]
    main(3, 1000)
    print("=====")
    main(5, 10000)
