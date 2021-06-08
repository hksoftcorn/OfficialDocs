def solution():
    n = int(input())
    m = int(input())
    k = int(input())
    ans = n * m * k
    arr = [0] * 10

    for ele in str(ans):
        arr[int(ele)] += 1
    
    for i in range(10):
        print(arr[i])

solution()