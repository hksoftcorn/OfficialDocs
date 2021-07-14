from collections import deque

V, E, K, S = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)

visited = [False] * (V + 1)
visited[S] = True
ans = []

Q = deque([(S, 0)])
while Q:
    node, cnt = Q.popleft()
    if cnt == K:
        ans.append(node)
    elif cnt < K:
        for w in G[node]:
            if not visited[w]:
                visited[w] = True
                Q.append((w, cnt + 1))
    else:
        break

if not ans:
    print(-1)    
else:
    for ele in sorted(ans):
        print(ele)
    