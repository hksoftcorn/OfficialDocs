V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x : x[2], reverse=True)

# find_set
p = [i for i in range(V + 1)]
def find_set(v):
    if v != p[v]:
        p[v] = find_set(p[v])
    return p[v]

# kruskal
ans = cnt = 0
while cnt < V - 1: # 간선의 수 : V - 1
    u, v, w = edges.pop()
    a, b = find_set(u), find_set(v)
    if a == b: continue
    p[b] = a
    cnt += 1
    ans += w

print(ans)