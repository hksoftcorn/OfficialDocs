def solution():
    N, P = map(int, input().split())
    my_set = set()
    n = N
    isN = False
    while n not in my_set:
        my_set.add(n)
        n = n * N % P

        if N == n:
            isN = True
    print(len(my_set) - 1 + isN)

solution()