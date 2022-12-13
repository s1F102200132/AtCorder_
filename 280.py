H,W = map(int,input().split())
result = 0
for i in range(H):
    S = list(input())
    for j in range(W):
        if S[j] == '#':
            result += 1
print(result)