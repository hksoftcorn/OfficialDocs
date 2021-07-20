import heapq

V, E = map(int, input().split())
enemy = list(map(int, input().split())) # 1은 x
enemy[-1] = 0
G = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

dist = [float('inf')] * V

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        d, u = heapq.heappop(Q)
        if dist[u] < d: continue

        for v, w in G[u]:
            if enemy[v]: continue
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(Q, (dist[v], v))

dijkstra(0)

if dist[V - 1] == float('inf'):
    print(-1)
else:
    print(dist[V - 1])