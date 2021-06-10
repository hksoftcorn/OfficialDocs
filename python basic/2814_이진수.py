def binaryToDecimal():
    binary = str(input())
    decimal = 0
    for i in range(len(binary)):
        decimal = 2 * decimal + int(binary[i])
    print(decimal)

binaryToDecimal()