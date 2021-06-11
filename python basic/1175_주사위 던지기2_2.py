def solution():
    n, m = map(int, input().split())
    arr = [0] * n
    def dice(level, cur_sum):
        if cur_sum > m:
            return
        if level == n:
            if cur_sum == m:
                print(' '.join(map(str, arr)))
            return
        for i in range(1, 7):
            arr[level] = i
            dice(level + 1, cur_sum + i)
    dice(0, 0)

solution()