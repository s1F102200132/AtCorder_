S = str(input())
T = str(input())
wk = 0
for i in range(len(S)):
    if S[i] != T[i]:
        print(i+1)
        wk = 1
        exit()
if wk == 0:
    print(len(S)+1)