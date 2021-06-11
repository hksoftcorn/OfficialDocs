def solution():
    A = input()
    B = input()
    C = input()
    D = input()
    E = input()
    max_length = max(len(A), len(B), len(C), len(D), len(E))
    ans = ''
    for i in range(max_length):
        if i < len(A):
            ans += A[i]
        if i < len(B):
            ans += B[i]
        if i < len(C):
            ans += C[i]
        if i < len(D):
            ans += D[i]
        if i < len(E):
            ans += E[i]
    print(ans)

solution()