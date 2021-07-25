import heapq

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
s, t = map(int, input().split())
dist = [float('inf')] * (V + 1)
path = [0] * (V+1)

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
                path[v] = u
                heapq.heappush(Q, (dist[v], v))

dijkstra(s)
print(path)
print(dist[t])