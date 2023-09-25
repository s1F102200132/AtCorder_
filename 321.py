N = int(input())
D = []
while N>0:
    D.append(N%10)
    N //= 10
D.reverse()

for i in range(1,len(D)):
    if D[i-1]<=D[i]:
        print("No")
        exit()

print("Yes")
