def isBoundary(x):
    if 2 > x or 9 < x:
        return -1
    else:
        return 1

def solution():
    a, b = map(int, input().split())
    if isBoundary(a) == -1 or isBoundary(b) == -1:
        return 'INPUT ERROR!'

    if a <= b: # 증가
        my_list = list(range(a, b + 1))
        for ele in my_list:
            for i in range(1, 10):
                if i * ele < 10:
                    print(f'{ele} * {i} =  {ele * i}', end='   ')
                else:
                    print(f'{ele} * {i} = {ele * i}', end='   ')
                if i % 3 == 0:
                    print()
            print()

    else: # 감소
        my_list = list(range(a, b - 1, -1))
        for ele in my_list:
            for i in range(1, 10):
                if i * ele < 10:
                    print(f'{ele} * {i} =  {ele * i}', end='   ')
                else:
                    print(f'{ele} * {i} = {ele * i}', end='   ')
                if i % 3 == 0:
                    print()
            print()

solution()