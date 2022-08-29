N = int(input())
A = set(map(int,input().split()))
S = {i for i in range(2010)}
T = S - A
print(min(T))
