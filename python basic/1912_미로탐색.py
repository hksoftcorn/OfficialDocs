def solution():
    n, m = map(int, input().split())
    G = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for _ in range(m):
        v, w = map(int, input().split())
        G[v].append(w)
        G[w].append(v)
    
    def dfs(v):
        visited[v] = 1
        print(v, end=' ')
        for w in sorted(G[v]):
            if visited[w]: continue
            dfs(w)

    # def dfs(v):
    #     Q = [v]
    #     visited[v] = 1
    #     while Q:
    #         cur_v = Q.pop()
    #         print(cur_v, end=' ')
    #         for w in sorted(G[cur_v], reverse=True):
    #             if not visited[w]:
    #                 visited[w] = 1
    #                 Q.append(w)

    dfs(1)

solution()