def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, n):
        selected_num = arr[i]
        for j in range(i):
            if selected_num < arr[j]:
                arr.insert(j, selected_num)
                arr.pop(i + 1)
                break
        print(' '.join(map(str, arr)))

solution()  