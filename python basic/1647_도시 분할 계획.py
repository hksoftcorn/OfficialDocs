V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2], reverse=True)
# find_set
p = [i for i in range(V + 1)]
def find_set(v):
    if v != p[v]:
        p[v] = find_set(p[v])
    return p[v]
# kruskal
cnt = ans = max_w = 0
while cnt < V - 1: # 간선의 수 = V - 1 
    u, v, w = edges.pop()
    a, b = find_set(u), find_set(v)
    if a == b: continue
    p[b] = a
    cnt += 1
    ans += w
    max_w = max(max_w, w)

print(ans - max_w)


"""prim : 시간초과
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))
visited = [0] * (V + 1)
key = [0xfffff] * (V + 1)
key[1] = 0
ans = 0
max_key = 0
for _ in range(V):
    u, min_key = 0, 0xfffff
    for i in range(1, V + 1):
        if not visited[i] and min_key > key[i]:
            u, min_key = i, key[i]
    visited[u] = 1
    ans += key[u]
    max_key = max(max_key, key[u])

    for v, w in G[u]:
        if not visited[v] and key[v] > w:
            key[v] = w

print(ans - max_key)
"""