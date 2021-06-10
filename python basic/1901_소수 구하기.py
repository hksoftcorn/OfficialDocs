number = 1000001
arr = [1] * number
# 소수 판별
arr[1] = 0
for i in range(2, number):
    if arr[i] == 0: continue
    for j in range(i + i, number, i):
        arr[j] = 0

def solution():
    n = int(input())
    if arr[n]:
        print(n)
        return
    for i in range(1, n):
        if arr[n-i] and arr[n+i]:
            print(n-i, n+i)
            return
        elif arr[n-i]:
            print(n-i)
            return
        elif arr[n+i]:
            print(n+i)
            return

for tc in range(1, int(input()) + 1):
    solution()

