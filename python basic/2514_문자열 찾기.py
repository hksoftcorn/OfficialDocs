def solution():
    input_data = input()
    cnt1 = 0
    cnt2 = 0
    for i in range(len(input_data) - 2):
        string = input_data[i : i + 3]
        if string == 'KOI':
            cnt1 += 1
        elif string == 'IOI':
            cnt2 += 1
    print(cnt1)
    print(cnt2)

solution()