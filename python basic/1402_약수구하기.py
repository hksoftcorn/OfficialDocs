def solution():
    n, m = map(int, input().split())
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    result += [n]
    if len(result) < m:
        print(0)
    else:
        print(result[m - 1])

solution()