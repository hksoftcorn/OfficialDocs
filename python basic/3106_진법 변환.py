def xToDecimal(x : int, numbers : list) -> int:
    ten = 0
    for i in range(len(numbers)):
        if numbers[i].isdigit():
            ten = x * ten + int(numbers[i])
        else:
            ten = x * ten + ord(numbers[i]) - 55
    return ten

def yFromDecimal(y : int, ten : int) -> str:
    n = ten
    ans = ''
    while n:
        q, r = divmod(n, y)
        if r >= 10:
            ans = chr(r + 55) + ans
        else:
            ans = str(r) + ans
        n = q
    return ans

def solution():
    while 1:
        input_data = list(input().split())
        if len(input_data) == 1:
            return
        n, numbers, m = input_data
        ten = xToDecimal(int(n), numbers)
        ans = yFromDecimal(int(m), ten)
        print(ans if len(ans) else 0)

solution()