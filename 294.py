N = int(input())
A = list(map(int,input().split()))
for i in A:
    if i % 2 == 0:
        print(i, end=' ')