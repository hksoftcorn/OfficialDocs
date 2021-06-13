def solution():
    n = int(input())
    stack = []
    i = 0

    def func_stack(s):
        if s == 'o':
            if not stack:
                print('empty')
            else:
                print(stack.pop())
        elif s== 'c':
            print(len(stack))

    while i < n:
        input_data = list(input().split())
        if len(input_data) > 1:
            stack += [int(''.join(input_data[1:]))]
        else:
            func_stack(input_data[0])
        i += 1

solution()