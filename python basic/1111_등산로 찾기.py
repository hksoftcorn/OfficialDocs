from collections import deque

N = int(input())
mi, mj = map(int, input().split()) # 정상 위치
arr = [list(map(int, input().split())) for _ in range(N)]
dist = [[0xfffffff] * N for _ in range(N)]

def bfs(v):
    r, c = v
    dist[r][c] = arr[r][c] ** 2
    Q = deque([(r, c)])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def cal_cost(cur_r, cur_c, nr, nc):
        cur_ = arr[cur_r][cur_c]
        next_ = arr[nr][nc]

        if cur_ >= next_:
            return cur_ - next_
        else:
            return (next_ - cur_) ** 2

    while Q:
        cur_r, cur_c = Q.popleft()

        for i in range(4):
            nr, nc = cur_r + dr[i], cur_c + dc[i]
            # if 0 <= nr < N and 0 <= nc < N:
            if 0 > nr or nr >= N or 0 > nc or nc >= N: continue
            cost = cal_cost(cur_r, cur_c, nr, nc)
            if dist[nr][nc] > dist[cur_r][cur_c] + cost:
                dist[nr][nc] = dist[cur_r][cur_c] + cost
                Q.append((nr, nc))

for r in range(N):
    for c in range(N):
        if r == 0 or r == N or c == 0 or c == N:
            bfs((r, c))

print(dist[mi - 1][mj - 1])