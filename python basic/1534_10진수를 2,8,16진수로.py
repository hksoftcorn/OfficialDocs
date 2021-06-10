def solution():
    n, m = map(int, input().split())
    ans = ''
    if m == 2:
        while n:
            q, r = divmod(n, 2)
            ans = str(r) + ans
            n = q
        print(ans)
    elif m == 8:
        while n:
            q, r = divmod(n, 8)
            ans = str(r) + ans
            n = q
        print(ans)
    elif m == 16:
        while n:
            q, r = divmod(n, 16)
            if r >= 10:
                if r == 10:
                    ans = 'A' + ans
                if r == 11:
                    ans = 'B' + ans
                if r == 12:
                    ans = 'C' + ans
                if r == 13:
                    ans = 'D' + ans
                if r == 14:
                    ans = 'E' + ans
                if r == 15:
                    ans = 'F' + ans
            else:
                ans = str(r) + ans
            n = q
        print(ans)

solution()