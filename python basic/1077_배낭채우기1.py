# Sample input 
# N, W = 4, 14 
# J = [[2, 40], [5, 110], [10, 220], [3, 50]] # weight, value

N, W = map(int, input().split())
J = []
for _ in range(N):
    J.append([int(x) for x in input().split()])

C = []
for w in range(W+1): 
    maxCost = 0 
    for i in range(N): 
        # weight 체크 and value 체크
        if w - J[i][0] >= 0 and C[w-J[i][0]] + J[i][1] > maxCost:
            maxCost = C[w-J[i][0]] + J[i][1]
    C.append(maxCost) 

print(C)

