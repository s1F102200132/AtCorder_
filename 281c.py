N,T = map(int,input().split())
A = list(map(int,input().split()))
time = 0

while time <= T:
    for i in range(N):
        time += A[i]
        if time >= T:
            break
print(i+1,time-T)
            
    


