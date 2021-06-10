def solution():
    input_data = list(map(int, input().split()))
    n = input_data[0]
    numbers = input_data[1:]
    arr = [0] * 6
    def comb(N, k):
        if k == 0:
            print(arr)
        else:
            arr[k - 1] = numbers[N - 1]
            comb(N-1, k-1)
            comb(N-1, k)
    comb(n, 6)

solution()           

# 7 1 2 3 4 5 6 7
# 8 1 2 3 5 8 13 21 34


# def solution():
#     input_data = list(map(int, input().split()))
#     n = input_data[0]
#     numbers = input_data[1:]
#     visited = [0] * n
#     # arr = [0] * 6
#     def comb(level):
#         if level == 6:
#             for l in range(n):
#                 if visited[l]: print(numbers[l], end=' ')
#             # print(' '.join(map(str, arr)))
#             print()
#             return

#         for i in range(level, n):
#             if visited[i]: continue
#             visited[i] = 1
#             # arr[level] = numbers[i]
#             comb(level + 1)
#             visited[i] = 0
#     comb(0)

# solution()           
# # 7 1 2 3 4 5 6 7
# # 8 1 2 3 5 8 13 21 34