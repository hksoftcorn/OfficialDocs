n = int(input())
dp = [0] * 10000000
dp[1] = 1
dp[2] = 2
def tile(n):
    if n <= 2:
        return dp[n]
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(tile(n) % 10007)
    