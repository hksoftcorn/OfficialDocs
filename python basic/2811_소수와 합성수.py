number = 1000000001
arr = [1] * number
for i in range(2, number):
    if arr[i] == 0: continue
    for j in range(i + i, number, i):
        arr[j] = 0

def solution():
    input_data = list(map(int, input().split()))
    for ele in input_data:
        if arr[ele]:
            print('prime number')
        elif ele == 1:
            print('number one')
        else:
            print('composite number') 

solution()