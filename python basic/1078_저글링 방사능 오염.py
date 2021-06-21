m, n = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
zc, zr = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
total_time = 0

def bfs(r, c):
    # from collections import deque
    global total_time, arr
    Q = [(r, c)]
    visited[r][c] = 3

    while Q:
        cur_r, cur_c = Q.pop(0)
        arr[cur_r][cur_c] = '0'
        total_time = max(total_time, visited[cur_r][cur_c])
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and arr[nr][nc] == '1':
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
                    Q.append((nr, nc))

    print(total_time)

bfs(zr - 1, zc - 1)
print(sum([ele.count('1') for ele in arr]))
