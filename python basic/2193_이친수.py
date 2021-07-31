# 1 <= n <= 90 자리 수
n = int(input())
dp = [0] * (n + 1)

def solution(n):
    if n <= 0: return 0
    if n == 1: return 1
    if dp[n]: 
        return dp[n]
    else:
        dp[n] = solution(n - 1) + solution(n - 2)
        return dp[n]

print(solution(n))