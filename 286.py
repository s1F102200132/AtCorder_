N,P,Q,R,S = map(int,input().split())
A = list(map(int,input().split()))
for i in range(P,Q+1):
    A[i-1],A[R-P+i-1]=A[R-P+i-1],A[i-1]
print(*A)


