# def dfs(v):
#     global cnt, n, m, visited
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]

#     cur_r, cur_c = v
#     visited[cur_r][cur_c] = 1
#     for i in range(4):
#         nr = cur_r + dr[i]
#         nc = cur_c + dc[i]
#         if 0 <= nr < n and 0 <= nc < m:
#             if not visited[nr][nc] and arr[nr][nc] == 0:
#                 cnt += 1
#                 print(cnt)
#                 dfs((nr, nc))

cnt = 0
def solution():
    global cnt
    n, m, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    

    for _ in range(k):
        lx, ly, rx, ry = map(int, input().split())
        for i in range(rx - lx):
            for j in range(ry - ly):
                arr[ly + j][lx + i] = 1
    # print(arr)

    def dfs(v):
        global cnt
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        cur_r, cur_c = v
        visited[cur_r][cur_c] = 1
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and arr[nr][nc] == 0:
                    cnt += 1
                    dfs((nr, nc))

    result = []
    for r in range(n):
        for c in range(m):
            if not visited[r][c] and arr[r][c] == 0:
                cnt = 1
                dfs((r, c))
                result.append(cnt)
                
    print(len(result))
    print(' '.join(map(str, sorted(result))))

solution()