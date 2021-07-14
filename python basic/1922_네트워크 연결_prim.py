V = int(input())
E = int(input())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))
visited = [False] * (V + 1)
key = [0xffffff] * (V + 1)
key[1] = 0
ans = 0

for _ in range(V):
    u, min_key = 1, 0xffffff
    for i in range(1, V + 1):
        if not visited[i] and min_key > key[i]:
            u, min_key = i, key[i]
    visited[u] = True
    ans += key[u]

    for v, w in G[u]:
        if not visited[v] and key[v] > w:
            key[v] = w

print(ans)