N = int(input())
A =list(map(int,input().split()))
Q = int(input())
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        type,k,x = query
        A[k - 1] = x
    else:
        type,k = query
        print(A[k - 1])
    

