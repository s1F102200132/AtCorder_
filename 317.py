N,H,X = list(map(int,input().split()))
P = [*map(int, input().split())]
for n in range(N):
    if H+P[n] >= X:
        print(n+1)
        exit(0)

    

