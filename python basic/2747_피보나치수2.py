n = int(input())
fibo = [0] * 100
fibo[0] = 0
fibo[1] = 1
fibo[2] = 1

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    for i in range(3, n + 1):
        fibo[i] = fibo[i - 2] + fibo[i - 1]
    print(fibo[i])
