N,T = map(int,input().split())
A = list(map(int,input().split()))
number = 0
time = 0

while time <= T:
    for i in range(N):
        time += A[i]
    break
print(i+1,time)

