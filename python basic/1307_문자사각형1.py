"""
>>> print(ord('A'))
65  
>>> print(ord('Z')) 
90  
"""
def numToChar(number):
    number -= 65
    r = number % 26
    return chr(r + 65)

def solution():
    n = int(input())
    for i in range(n):
        number = 65 + n * n - 1 - i
        for j in range(n):
            print(numToChar(number - n * j), end=' ')
        print()

solution()