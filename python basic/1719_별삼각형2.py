def solution():
    n, m = map(int, input().split())
    if (1 > n or n > 100 or n % 2 == 0) or (1 > m or m > 4):
        print('INPUT ERROR!')
        return 
    mid = n // 2

    if m == 1:
        for i in range(n):
            for j in range(mid - abs(mid - i) + 1):
                print('*', end=' ')
            print()
    elif m == 2:
        for i in range(n):
            print(' ' * abs(mid - i) * 2 + '* ' * (mid - abs(mid - i) + 1))
    elif m == 3:
        for i in range(n):
            print(' ' * 2 * (mid - abs(mid - i)) + '* ' * (2 * abs(mid - i) + 1))
    elif m == 4:
        for i in range(n):
            if i < mid:
                print(' ' * 2 * (mid - abs(mid - i)) + '* ' * (abs(mid - i) + 1))
            elif i > mid:
                print(' ' * (n - 1) + '*', end=" ")
                print('* ' * (abs(mid - i)))
            else:
                print(' ' * (n - 1) + '*')


solution()