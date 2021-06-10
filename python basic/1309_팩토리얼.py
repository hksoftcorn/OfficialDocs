def solution():
    n = int(input())
    ans = 1
    for i in range(n, 0, -1):
        if i > 1:
            ans *= i
            print(f'{i}! = {i} * {i-1}!')
        else:
            print(f'{i}! = {i}')
    print(ans)

solution()