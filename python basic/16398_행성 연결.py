V = int(input())
edges = []
for i in range(V):
    input_data = list(map(int, input().split()))
    for j in range(i + 1, V):
        # u, v, w
        edges.append((i+1, j+1, input_data[j]))
edges.sort(key=lambda x: x[2], reverse=True)
# find_set
p = [i for i in range(V+1)]
def find_set(v):
    if v != p[v]:
        p[v] = find_set(p[v])
    return p[v]
# kruskal
ans = cnt = 0
while cnt < V - 1:
    u, v, w = edges.pop()
    a, b = find_set(u), find_set(v)
    if a == b: continue
    p[b] = a
    cnt += 1
    ans += w

print(ans)

""" prim
G = [[] for _ in range(V + 1)]
for i in range(V):
    input_data = list(map(int, input().split()))
    for j in range(i + 1, V):
        v = i + 1
        u = j + 1
        w = input_data[j]
        G[v].append((u, w))
        G[u].append((v, w))

visited = [False] * (V + 1)
key = [0xfffff] * (V + 1)
key[1] = 0
ans = 0

for _ in range(V):
    u, min_key = 1, 0xfffff
    for i in range(1, V + 1):
        if not visited[i] and min_key > key[i]:
            u, min_key = i, key[i]
    
    visited[u] = True
    ans += key[u]
    for v, w in G[u]:
        if not visited[v] and key[v] > w:
            key[v] = w

print(ans)
"""