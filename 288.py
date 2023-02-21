N = int(input())
arrAB = [list(map(int,input().split()))for i in range(N)]

for a,b in arrAB:
    print(a + b)
