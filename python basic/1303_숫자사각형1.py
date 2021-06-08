def solution():
    n, m = list(map(int, input().split()))
    for i in range(1, n * m + 1):
        print(i, end=" ")
        if i % m == 0:
            print()

solution()