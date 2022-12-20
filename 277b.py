N = int(input())
flag = True
for i in range(N):
    S = input()
    if S[0] != 'H' or 'D' or 'C' or 'S':
        flag = False
    if S[1] != 'A'or '2' or '3 'or '4' or '5' or '6' or '7' or '8' or '9' or 'T' or 'J' or 'Q' or 'K':
        flag = False
for i in range(N-1):
    if S[i] == S[i]:
        flag = False
        
    
print('No' if flag==False else 'Yes')

