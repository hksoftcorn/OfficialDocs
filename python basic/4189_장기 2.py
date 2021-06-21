def solution():
    n, m = map(int, input().split())
    kr, kc, pr, pc = map(int, input().split()) # k = Knight, p = Pawn
    # n = m = 99
    # kr, kc, pr, pc = 3, 5, 2, 8
    if kr == pr and kc == pc:
        print(0)
        return

    arr = [[0] * m for _ in range(n)]
    arr[pr - 1][pc - 1] = 1

    visited = [[0] * m for _ in range(n)]

    dr = [1, 1, 2, 2, -1, -1, -2, -2]
    dc = [-2, 2, -1, 1, -2, 2, -1, 1]
    
    def bfs(r, c):
        from queue import Queue
        Q = Queue()
        Q.put((r, c))
        visited[r][c] = 1

        while Q:
            cur_r, cur_c = Q.get()
            if arr[cur_r][cur_c] == 1:
                return visited[cur_r][cur_c]

            for i in range(8):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]
                if 0 > nr or nr >= n or 0 > nc or nc >= m: continue
                # if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
                    Q.put((nr, nc))

    print(bfs(kr - 1, kc - 1) - 1)


solution()