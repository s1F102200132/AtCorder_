H,W = map(int,input().split())
S = [[] for _ in range(W)]
T = [[] for _ in range(W)]
for i in range(H):
    row = list(input())
    for j in range(W):
        S[j].append(row[j])

for i in range(H):
    row = list(input())
    for j in range(W):
        T[j].append(row[j])
S = sorted(S)
T = sorted(T)
if S == T:
    print('Yes')
else:
    print('No')