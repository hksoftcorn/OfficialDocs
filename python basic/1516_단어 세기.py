def solution():
    while True:
        input_data = input()
        result = {}
        if input_data == 'END':
            return

        for key in input_data.split():
            result[key] = result.get(key, 0) + 1

        for key in sorted(result.keys()):
            print(f'{key} : {result[key]}')

solution()