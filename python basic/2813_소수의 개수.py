def solution():
    n, m = map(int, input().split())
    number = 2000001
    arr = [1] * number
    # 소수 판별
    arr[1] = 0
    for i in range(2, number):
        if arr[i] == 0: continue
        for j in range(i + i, number, i):
            arr[j] = 0

    cnt = 0
    for k in range(n, m + 1):
        if arr[k]:
            cnt += 1
    print(cnt)

solution()