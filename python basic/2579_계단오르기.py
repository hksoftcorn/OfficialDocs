n = int(input()) # 1 <= n <= 300
steps = [0] + [int(input()) for _ in range(n)]
# print(steps)
memo = [0] * (n + 1)

def dp(n):
    if n == 1:
        return steps[1]
    elif n == 2:
        return steps[1] + steps[2]
    elif n == 3:
        return max(steps[1] + steps[3], steps[2] + steps[3])
    else:
        memo[1] = steps[1]
        memo[2] = steps[1] + steps[2]
        memo[3] = max(steps[1] + steps[3], steps[2] + steps[3])
        for i in range(4, n + 1):
            memo[i] = max(memo[i - 2] + steps[i], memo[i - 3] + steps[i - 1] + steps[i])
        return memo[n]
print(dp(n))