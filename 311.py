N = int(input())
S = str(input())
abc = set()
for i in range(N):
    abc.add(S[i])
    if len(abc) == 3:
        print(i +1)
        break
    
