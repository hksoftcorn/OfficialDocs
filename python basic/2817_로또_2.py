def solution():
    input_data = list(map(int, input().split()))
    n = input_data[0]
    numbers = input_data[1:]
    arr = [0] * 6
    visited = [0] * 50

    def comb(level, k):
        if level == 6:
            print(' '.join(map(str, arr)))
            return

        for i in range(k, n):
            number = numbers[i]
            if visited[number]: continue
            visited[number] = 1
            arr[level] = number
            comb(level + 1, i)
            visited[number] = 0
            
    comb(0, 0)

solution()