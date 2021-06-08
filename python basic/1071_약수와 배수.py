def solution():
    n = int(input())
    input_data = list(map(int, input().split()))
    input_data.sort()
    m = int(input())

    first_ans = 0
    second_ans = 0
    for ele in input_data:
        if ele <= m and m % ele == 0:
            first_ans += ele
        if ele >= m and ele % m == 0:
            second_ans += ele
    print(first_ans)
    print(second_ans)

solution()