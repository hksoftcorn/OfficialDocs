def solution():
    n, m = map(int, input().split())
    arr = [0] * n
    def dice1(level):
        if level == n:
            print(' '.join(map(str, arr)))
            return
        for i in range(1, 7):
            arr[level] = i
            dice1(level + 1)
    
    def dice2(level, k):
        if level == n:
            print(' '.join(map(str, arr)))
            return
        else:
            for i in range(k, 7):
                arr[level] = i
                dice2(level + 1, i)

    visited = [0] * 7
    def dice3(level):
        if level == n:
            print(' '.join(map(str, arr)))
            return
        for i in range(1, 7):
            if visited[i]: continue
            visited[i] = 1
            arr[level] = i
            dice3(level + 1)
            visited[i] = 0

    if m == 1:
        dice1(0)
    elif m == 2:
        dice2(0, 1)
    elif m == 3:
        dice3(0)

solution()