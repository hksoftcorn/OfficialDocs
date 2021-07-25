"""MST : kruskal"""
# N, K = 4, 2
# edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
# edges.sort(key=lambda x: x[2], reverse=True)

# # find_set
# p = [i for i in range(N + 1)]
# def find_set(v):
#     if v != p[v]:
#         p[v] = find_set(p[v])
#     return p[v]

# # kruskal
# ans = cnt = 0
# while cnt < N - 1:
#     u, v, w = edges.pop()
#     a, b = find_set(u), find_set(v)
#     if a == b: continue
#     p[b] = a
#     cnt += 1
#     ans += w

# print(ans)

"""Dijkstra"""
import heapq
N, K = 4, 2
G = [[] for _ in range(N + 1)]
info = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
for u, v, w in info:
    G[u].append((v, w))
dist = [float('inf')] * (N + 1)

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        d, u = heapq.heappop(Q)
        if dist[u] < d: continue

        for v, w in G[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(Q, (dist[v], v))

dijkstra(K)
ans = max(dist[1:])
if ans == float('inf'):
    print(-1)
else:
    print(ans)