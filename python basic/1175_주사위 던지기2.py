def solution():
    n, m = map(int, input().split())
    if m == 1:
        return

    arr = [0] * n 
    def perm(level, cur_sum):
        if level == n:
            if cur_sum == m:
                print(' '.join(map(str, arr)))
            return

        for i in range(1, 7):
            arr[level] = i
            perm(level + 1, cur_sum + i)
    perm(0, 0)

solution()