N, M = map(int, input().split())
p = [i for i in range(N + 1)]
rank = [0] * (N + 1)
ans = N

def find_set(v):
    if v != p[v]:
        p[v] = find_set(p[v])
    return p[v]

for _ in range(M):
    u, v = map(int, input().split())
    a, b = find_set(u), find_set(v)
    if a == b: continue
    if rank[a] > rank[b]: 
        p[b] = a
    else: 
        p[a] = b
        if rank[a] == rank[b]: 
            rank[b] += 1

cnt = 0
for i in range(1, N + 1):
    if i == find_set(i):
        cnt += 1
print(cnt)
