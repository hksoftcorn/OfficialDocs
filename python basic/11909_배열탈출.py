import heapq
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dist = [[float('inf')] * N for _ in range(N)]

def dijkstra(r, c):
    Q = []
    heapq.heappush(Q, (0, r, c))
    dist[r][c] = 0
    move = [(1, 0), (0, 1)]

    while Q:
        d, cur_r, cur_c = heapq.heappop(Q)
        if dist[cur_r][cur_c] < d: continue

        for dr, dc in move:
            nr, nc = cur_r + dr, cur_c + dc
            if nr == N or nc == N: continue
            cost = arr[nr][nc] - arr[cur_r][cur_c] + 1 if arr[cur_r][cur_c] <= arr[nr][nc] else 0
            if dist[nr][nc] > dist[cur_r][cur_c] + cost:
                dist[nr][nc] = dist[cur_r][cur_c] + cost
                heapq.heappush(Q, (dist[nr][nc], nr, nc))

dijkstra(0, 0)
print(dist[N - 1][N - 1])