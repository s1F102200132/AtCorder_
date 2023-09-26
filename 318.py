N,M,P = list(map(int,input().split()))
if N > M:
    answer = N - M
    result = answer // P
    print(result + 1)
else:
    print(0)