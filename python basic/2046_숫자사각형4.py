def solution():
    n, m = list(map(int, input().split()))
    my_list = list(range(1, n + 1))
    if m == 1:
        for i in range(1, n + 1):
            for _ in range(n):
                print(i, end=' ')
            print()
    elif m == 2:
        for i in range(n):
            if i % 2 == 0:
                print(' '.join(map(str, my_list)))
            else:
                print(' '.join(map(str, my_list[::-1])))

    elif m == 3:
        for i in range(1, n + 1):
            new_list = list(map(lambda x : x * i, my_list))
            print(' '.join(map(str, new_list)))
        print()

solution()