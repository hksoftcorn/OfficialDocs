from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global max_cnt
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    Q = deque([(r, c)])

    while Q:
        cur_r, cur_c = Q.popleft()
        max_cnt = max(max_cnt, visited[cur_r][cur_c])

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 'L' and not visited[nr][nc]:
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
                    Q.append((nr, nc))

result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            max_cnt = 0
            bfs(i, j)
            result = max(result, max_cnt)

print(result - 1)