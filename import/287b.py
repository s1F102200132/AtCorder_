ans = 0
N,M = map(int,input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for i in range(N):
    flag = False
    for j in range(M):
        if S[i][-3:] == T[j]:
            flag = True
    if flag:
        ans += 1
print(ans)
