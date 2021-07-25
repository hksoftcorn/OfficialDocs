# import pprint
N, W = map(int, input().split())
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    weight, value = map(int, input().split())
    for j in range(1, W + 1):
        if weight > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i -1][j - weight] + value)

# pprint.pprint(dp)
print(dp[N][W])