V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

visited = [False] * (V + 1)
dist = [0xfffffff] * (V + 1)
dist[1] = 0
p = [0] * (V + 1)

for _ in range(V):
    u, min_key = 1, 0xfffffff
    for i in range(1, V+1):
        if not visited[i] and min_key > dist[i]:
            u, min_key = i, dist[i]
    visited[u] = True
    
    for v, w in G[u]:
        if not visited[v] and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            p[v] = u

print(dist[V])


