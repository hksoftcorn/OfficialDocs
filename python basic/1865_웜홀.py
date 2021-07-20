T = int(input())
for tc in range(1, T + 1):
    V, E, W = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    for _ in range(W):
        u, v, w = map(int, input().split())
        edges.append((u, v, -w))
    
    dist = [float('inf')] * (V + 1)

    def bellman_ford(start):
        dist[start] = 0
        for i in range(V):
            for j in range(E + W):
                u, v, w = edges[j]
                if dist[u] != float('inf') and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    if i == V - 1:
                        return True
        return False
    
    isNegative = bellman_ford(1)
    
    ans = 'NO'
    if isNegative:
        ans = 'YES'
    else:
        for i in range(2, V + 1):
            if dist[i] == float('inf'):
                ans = 'YES'
    print(ans)

