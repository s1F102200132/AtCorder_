n,k= map(int, input().split())
 
ans = []
for i in range(n):
    if i < k:
        ans.append(input())
    else:
        c = input()
 
ans.sort()
 
for i in ans:
    print(i)
