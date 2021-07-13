# Kruskal -> sort & find_set
N = int(input())
edges = []
G = [[] for _ in range(N)]

for i in range(N):
    weights = list(map(int, input().split()))
    for j in range(i + 1, N):
        edges.append((i, j, weights[j]))
    for k in range(N):
        if i == k: continue
        G[i].append((k, weights[k]))
edges.sort(key=lambda x: x[2], reverse=True)
print(edges)

# find_set
p = [i for i in range(N)]
def find_set(v):
    if v != p[v]:
        p[v] = find_set(p[v])
    return p[v]
    
# Kruskal
cnt = ans = 0
while cnt < N - 1: # 간선의 수 = N - 1
    u, v, w = edges.pop()
    a, b = find_set(u), find_set(v)
    if a == b: continue
    p[b] = a
    cnt += 1
    ans += w

print(ans)
    
# Prim 
visited = [False] * N
key = [0xfffff] * N
key[0] = 0
ans = 0

for _ in range(N):
    u, min_key = 0, 0xffff
    for i in range(N):
        if not visited[i] and min_key > key[i]:
            u, min_key = i, key[i]
    
    visited[u] = True
    ans += key[u]

    for v, w in G[u]:
        if not visited[v] and key[v] > w:
            key[v] = w

print(ans)