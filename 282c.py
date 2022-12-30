N = int(input())
S = list(input())
lef_even = True
for i in range(N):
    if lef_even and S[i] == ',':
        S[i] = '.'
    if S[i] == '"':
        lef_even = not lef_even
print("".join(S))
    
