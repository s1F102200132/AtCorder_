N = int(input())
S = [str(input()) for i in range(N)]
result = []
for j in S:
    result.append(j)
if result.count('For') >= result.count('Against'):
    print('Yes')
else:
    print('No')