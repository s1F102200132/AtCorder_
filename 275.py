n=int(input())
h=list(map(int, input().split()))
ans=1
for i in range(2,len(h)+1):
    if(h[ans-1]<h[i-1]):
      ans=i
print(ans)