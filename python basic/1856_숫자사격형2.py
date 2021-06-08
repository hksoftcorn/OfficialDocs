def solution():
    n, m = list(map(int, input().split()))
    tmp = ''
    for i in range(1, n * m + 1):
        if ((i-1) // m) % 2 == 0:
            tmp = tmp + str(i) + ' '
        else:
            tmp = str(i) + ' ' + tmp
        if i % m == 0:
            print(tmp)
            tmp = ''
solution()