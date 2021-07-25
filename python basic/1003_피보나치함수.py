for tc in range(int(input())):
    n = int(input())
    count = [0] * 2
    memo = [[] for _ in range(41)]
    memo[0] = [1, 0]
    memo[1] = [0, 1]
    
    def fibo(n):
        if n < 2:
            return 
        for i in range(2, n + 1):
            a = memo[i - 1][0] + memo[i - 2][0]
            b = memo[i - 1][1] + memo[i - 2][1]
            memo[i] = [a, b]
    fibo(n)
    
    print(' '.join(map(str, memo[n])))