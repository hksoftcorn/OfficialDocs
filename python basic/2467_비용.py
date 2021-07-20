V, E = map(int, input().split())
edeges = [list(map(int, input().split())) for _ in range(E)]
edeges.sort(key=lambda x: x[2], reverse=True)
# find_set
p = [i for i in range(V + 1)]
def find_set(v):
    if v != p[v]:
        p[v] = find_set(p[v])
    return p[v]

# kruskal
ans = cnt = 0
while cnt < V - 1:
    u, v, w = edeges.pop()
    a, b = find_set(u), find_set(v)
    if a == b: continue
    p[b] = a
    ans += w
    cnt += 1

print(ans)
