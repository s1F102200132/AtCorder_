N = int(input())
S = list(str(input()))
l = 0
for i in range(N-1):
    if S[i] != S[i+1]:
        l += 1
print(l)



