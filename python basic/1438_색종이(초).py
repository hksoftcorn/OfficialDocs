matrix = [[0] * 101 for _ in range(101)]
for tc in range(1, int(input()) + 1):
    left, bottom = map(int, input().split())
    # r, c
    for i in range(10):
        r = left + i 
        for j in range(10):
            c = bottom + j
            if not matrix[r][c]:
                matrix[r][c] = 1
                
total = sum([sum(matrix[i]) for i in range(101)])
print(total)
