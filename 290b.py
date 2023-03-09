N,K = map(int,input().split())
S = (input())
win_cnt = 0
cnt = 0
result = []
ans = [0] * N
for i in S:
    if i == 'o':
        win_cnt += 1
        result.append(cnt)
    elif i == 'x':
        pass
    if win_cnt == K:
        break
    cnt += 1
for j in range(N):
    if j in result:
        ans[j] = 'o'
    else:
        ans[j] = 'x'

print(*ans,sep = '')