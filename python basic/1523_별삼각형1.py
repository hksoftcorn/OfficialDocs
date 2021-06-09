def solution():
    n, m = map(int, input().split())
    if (1 > n or n > 100) or (1 > m or m > 3):
        print('INPUT ERROR!')
        return 
    if m == 1:
        for i in range(n):
            for j in range(i+1):
                print("*", end='')
            print()
    elif m == 2:
        for i in range(n):
            for j in range(n - i):
                print("*", end='')
            print()
    elif m == 3:
        for i in range(n):
            tmp = ' ' * (n -1 - i) + '*' * i
            print(tmp + '*' + tmp[::-1])

solution()