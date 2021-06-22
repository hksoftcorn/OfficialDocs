"""
어떻게 bfs 여러 시작점을 같이 시작시키지?
-> 시간을 기준으로 한 칸씩 움직이는 것인가??

구체적인 해결방안
time 1초 : 배열 안의 1을 모두 찾는다, 1칸씩 bfs 움직인다.
time 2초 : 배열 안의 1을 모두 찾는다, 1칸씩 bfs 움직인다.

"""


from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global visited, max_cnt
    Q = deque([(r, c)])
    visited[r][c] = 1

    while Q:
        cur_r, cur_c = Q.popleft()
        max_cnt = max(max_cnt, visited[cur_r][cur_c])

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
                    arr[nr][nc] = 1
                    Q.append((nr, nc))

max_cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

if sum([ele.count(0) for ele in arr]):
    print(-1)
else:
    print(max_cnt - 1)
