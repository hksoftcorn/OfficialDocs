def solution():
    while True:
        number = str(input())
        if number == '0': return
        total = 0
        for num in number:
            total += int(num)
        print(int(number[::-1]), total)

solution()