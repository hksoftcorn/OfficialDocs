def solution():
    n, m = map(int, input().split())
    ans = [0] * n
    visited = [0] * 7
    def perm1(level):
        if level > n - 1:
            print(' '.join(map(str, ans)))
            return
        for i in range(1, 7):
            ans[level] = i
            perm1(level + 1)

    def perm2(level, k):
        if level > n - 1:
            print(' '.join(map(str, ans)))
            return
        for i in range(k, 7):
            ans[level] = i
            perm2(level + 1, i)

    def perm3(level):
        if level > n - 1:
            print(' '.join(map(str, ans)))
            return
        for i in range(1, 7):
            if visited[i]: continue
            visited[i] = 1
            ans[level] = i
            perm3(level + 1)
            visited[i] = 0

    if m == 1:
        perm1(0)
    elif m == 2:
        perm2(0, 1)
    elif m == 3:
        perm3(0)

solution()