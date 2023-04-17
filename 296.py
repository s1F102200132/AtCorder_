N = int(input())
S = list(str(input()))
flag = True
for i in range(N-1):
    if S[i] == S[i + 1]:
        flag = False
print('Yes' if flag else 'No')

