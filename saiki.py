N,X = map(int,input().split())

burger = 'p'
for i in range(N):
    burger = 'B' + burger + 'P' + burger + 'B'

print(burger[0:X].count('P'))