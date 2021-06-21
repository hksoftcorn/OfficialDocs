cnt = 0
def solution():
    global cnt
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    # print(arr)

    def dfs(v):
        global cnt
        dr = [-1, 1, 0 , 0]
        dc = [0, 0, -1, 1]
        cur_r, cur_c = v
        visited[cur_r][cur_c] = 1

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == '1' and not visited[nr][nc]:
                    cnt += 1
                    dfs((nr, nc))

    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '1' and not visited[i][j]:
                cnt = 1
                dfs((i, j))
                result.append(cnt)

    result.sort()
    print(len(result))
    for ele in result:
        print(ele)

solution()