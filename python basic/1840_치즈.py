def solution():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    def dfs(arr):
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = 1
        Q = [(0, 0)]
        while Q:
            cur_r, cur_c = Q.pop()
            for i in range(4):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if not visited[nr][nc]:
                        visited[nr][nc] = 1
                        if arr[nr][nc] == 1:
                            arr[nr][nc] = 0
                        else:
                            Q.append((nr, nc))

    while sum([sum(row) for row in arr]):
        total = sum([sum(row) for row in arr])
        dfs(arr)
        cnt += 1

    print(cnt)
    print(total)

solution()