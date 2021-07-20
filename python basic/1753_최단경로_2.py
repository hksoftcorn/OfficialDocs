# dijkstra 문제풀이 heap 사용해보기
import heapq

V, E = map(int, input().split())
K = int(input())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
dist = [0xfffffff] * (V + 1)

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        d, u = heapq.heappop(Q)
        if dist[u] < d: continue

        for ele in G[u]:
            v, w = ele
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(Q, (dist[v], v))

dijkstra(K)
for i in range(1, V + 1):
    if i == K:
        print(0)
    elif dist[i] == 0xfffffff:
        print('INF')
    else:
        print(dist[i])             