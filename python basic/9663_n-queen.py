n = int(input())
def is_available(cur_candidate, cur_c):
    cur_r = len(cur_candidate)
    # 현재 들어있는 후보자들의 길이로 놓을 자리의 row를 알 수 있습니다.
    # 현재까지 놓은 queen들의 자리들과 비교하며 cur_c가 들어갈 수 있는지 확인합니다
    for queen_row in range(cur_r):
        # 비교하는 조건은 다음과 같습니다.
        # 1) 놓은 queen과 똑같은 column에 위치하면 안 됩니다.
        # 2) 놓은 queen과 대각선 위치에 위치하면 안 됩니다.
        if cur_candidate[queen_row] == cur_c or abs(cur_candidate[queen_row] - cur_c) == cur_r - queen_row:
            return False
    return True

def DFS(N, cur_r, cur_candidate, result):
    if cur_r == N:
        result.append(cur_candidate[:])
        return
    # 퀸을 놓고 싶어요!
    # 컬럼을 하나하나 돌아가면서, 놓을 자리를 살펴봅니다.
    # 컬럼은 N개가 있습니다.
    for cur_c in range(N): 
        # 지금 뽑은 cur_r 이 놓을 수 있는 자리인가요? True or False
        if is_available(cur_candidate, cur_c):
            cur_candidate.append(cur_c)
            DFS(N, cur_r + 1, cur_candidate, result)
            cur_candidate.pop()

def solve_n_queen(N):
    result = []
    DFS(N, 0, [], result)
    return result

print(len(solve_n_queen(n)))

