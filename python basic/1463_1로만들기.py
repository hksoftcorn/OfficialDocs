N = int(input())
dp = [0] * 1000001
""" dp - 메모이제이션
def calc(n):
    if n == 1: return 0 
    if dp[n]: return dp[n]
    dp[n] = calc(n - 1) + 1

    if n % 3 == 0:
        dp[n] = min(dp[n], calc(n // 3) + 1)
    elif n % 2 == 0:
        dp[n] = min(dp[n], calc(n // 2) + 1)
    return calc(n)

print(calc(N))
"""
# 타뷸레이션
dp[0] = 10000001
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N + 1):
    a = 0; b = 0
    if i % 3 == 0:
        a = i // 3
    if i % 2 == 0:
        b = i // 2

    dp[i] = min(dp[i - 1] + 1, dp[a] + 1, dp[b] + 1)

print(dp[N])