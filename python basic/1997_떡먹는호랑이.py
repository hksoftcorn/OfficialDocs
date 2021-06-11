arr = [0] * 31
arr[0] = 1
arr[1] = 1
arr[2] = 2
idx = 3
while idx < 31:
    arr[idx] = arr[idx-1] + arr[idx-2]
    idx += 1

def solution():
    D, K = map(int, input().split())
    # arr[D-2] * Day2 + arr[D-3] * Day1
    a = arr[D-3]
    b = arr[D-2]
    for i in range(1, a):
        if (K - (a * i) ) % b == 0:
            print(i)
            print((K - (a * i) ) // b)
            return
            
solution()