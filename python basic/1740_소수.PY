number = 10001
arr = [1] * number
arr[1] = 0
# 소수 판별
for i in range(2, number):
    if arr[i] == 0: continue
    for j in range(i + i, number, i):
        arr[j] = 0

def solution():
    n = int(input())
    m = int(input())
    result = []
    for j in range(n, m+1):
        if arr[j]:
            result.append(j)
    if result:
        print(sum(result))
        print(result[0])
    else:
        print(-1)
    
solution()