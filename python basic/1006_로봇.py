"""
동서남북(1,2,3,4)
행 열 방향

명령 1. Go K
K : 1, 2, 3

명령 2. Turn dir
dir : left, right


* 설계
- 가장 빠른 길을 우선 찾는다 BFS
- 방향이 회전된 횟수를 세어줍니다
- 방향으로 칠해줍니다!!! -> 동서남북 1234
- 방향이 같은 부분에서 이동횟수를 3으로 나누어 횟수를 더해줍니다
"""
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

sr, sc, sd = map(int, input().split())
er, ec, ed = map(int, input().split())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(r, c, d): # d = direction
    # goal : bfs의 path를 찍자!!
    global visited
    Q = deque([(r, c)])
    visited[r][c] = str(d)
    
    while Q:
        cur_r, cur_c = Q.popleft()
        if cur_r == er - 1 and cur_c == ec - 1:
            return visited[cur_r][cur_c]

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 > nr or nr >= n or 0 > nc or nc >= m: continue
            if arr[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = visited[cur_r][cur_c] + str(i)
                Q.append((nr, nc))

result = bfs(sr - 1, sc - 1, sd - 1)
for 