n = int(input())
 
s = []
 
s =list(map(int, input().split()))
    
ans = []
ans.append(s[0])
for i in range(n-1):
    p = s[i+1] - s[i]
    ans.append(p)
 
for i in range(n):
    print(ans[i], end= ' ')