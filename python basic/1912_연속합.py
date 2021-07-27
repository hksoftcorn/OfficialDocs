n = int(input())
input_data = list(map(int, input().split()))
dp = [0] * n
dp[0] = input_data[0]

for i in range(1, n):
    x = input_data[i]
    dp[i] = max(dp[i - 1] + x, x)
print(max(dp))
