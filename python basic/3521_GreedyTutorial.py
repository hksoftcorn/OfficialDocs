# 1, 2, 4, 8, 16
a, b, c, d, e, N = map(int, input().split())
def solution():
    global N
    e_cnt = N // 16
        e_cnt = e
    N -= (16 * e_cnt)

    d_cnt = N // 8
    if d < d_cnt:
        d_cnt = d
    N -= (8 * d_cnt)

    c_cnt = N // 4
    if c < c_cnt:
        c_cnt = c
    N -= (4 * c_cnt)

    b_cnt = N // 2
    if b < b_cnt:
        b_cnt = b
    N -= (2 * b_cnt)

    a_cnt = N // 1
    if a < a_cnt:
        a_cnt = a
    N -= (1 * a_cnt)

    if N == 0:
        return a_cnt + b_cnt + c_cnt + d_cnt + e_cnt
    else:
        return 'impossible'

print(solution())
