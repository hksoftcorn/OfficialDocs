def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    def binary_search(array, target):
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = (low + high) // 2
            if array[mid] == target:
                return mid
            if  array[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    for ele in arr2:
        answer = binary_search(arr, ele)
        print(answer, end=' ')

solution()