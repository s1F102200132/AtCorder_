n = int(input())
a = list(map(int, input().split()))
for i in range(n-1, 0, -1):
  a[i] -= a[i-1]
print(*a)
