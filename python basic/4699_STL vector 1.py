n = int(input())
result = []

for _ in range(n):
    input_data = list(map(int, input().split()))
    result.append(input_data[1:])

output_index = list(map(int, input().split()))
for index in output_index:
    print(' '.join(map(str, result[index])))