# Sample input 
# N, W = 4, 14 
# J = [[2, 40], [5, 110], [10, 220], [3, 50]] # weight, value

N, W = map(int, input().split())
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = map(int, input().split())
    for j in range(1, W + 1): # 현재 담을 수 있는 가방의 무게
        if weight > j: # 현재 아이템의 무게 > 현재 담을 수 있는 가방의 무게라면,
            # 그 전에 담았던 무게로 덮어씁니다.
            dp[i][j] = dp[i - 1][j]
        else: # 담을 수 있는 무게라면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
print(dp[N][W])

