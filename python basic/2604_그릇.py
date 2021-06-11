def solution():
    input_data = input()
    total = 10
    pre_dish = input_data[0]
    for i in range(len(input_data) - 1):
        if pre_dish == input_data[i + 1]:
            total += 5
        else:
            total += 10
        pre_dish = input_data[i + 1]
    print(total)

solution()