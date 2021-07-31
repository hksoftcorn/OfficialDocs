def is_promising(v):
    for i in range(v):
        if row[v] == row[i] or abs(row[v] - row[i]) == v - i:
            return False
    return True

def dfs(v):
    global cnt
    if v == N:
        cnt += 1
        result.append(row[:])
    else:
        for i in range(N):
            row[v] = i
            if is_promising(v):
                dfs(v + 1)

N = int(input())
cnt = 0
row = [0] * N
result = []
dfs(0)
print(result)