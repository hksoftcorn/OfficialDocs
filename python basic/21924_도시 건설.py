V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2], reverse=True)
total = sum([ele[2] for ele in edges])
# find_set
p = [i for i in range(V + 1)]
def find_set(v):
    if v != p[v]:
        p[v] = find_set(p[v])
    return p[v]
# kruskal
ans = cnt = result = 0
while cnt < V - 1:
    if not edges:
        result = -1
        break
    u, v, w = edges.pop()
    a, b = find_set(u), find_set(v)
    if a == b: continue
    p[b] = a
    cnt += 1
    ans += w

if result != -1:
    result = total - ans
print(result)

