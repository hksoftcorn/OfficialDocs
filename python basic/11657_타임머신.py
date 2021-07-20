V, E = map(int, input().split()) # 노드 수, 간선 수 입력 받기
edges = [] # 모든 간선에 대한 정보를 담는 리스트 생성

# 그래프 생성
for _ in range(E):
    u, v, w = map(int, input().split()) # 노드, 인접 노드, 가중치
    edges.append((u, v, w))

dist = [float('inf')] * (V + 1) # 최단 거리 테이블을 모두 무한으로 초기화

def bellman_ford(start):
    dist[start] = 0
    for i in range(V): # 모든 노드
        for j in range(E): # 모든 간선
            u, v, w = edges[j]
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if i == V - 1:
                    return True
    return False

negative_cycle = bellman_ford(1)
if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, V + 1):
        if dist[i] == float('inf'): # 도달할 수 없는 경우 -1 출력
            print('-1')
        else: # 도달할 수 있는 겨우 거리를 출력
            print(dist[i])