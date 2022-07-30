H,W = map(int,input().split())
R,C = map(int,input().split())

result = 0

if 1 <= R-1:
    result += 1

if R+1 <= H:
    result += 1

if 1 <= C-1:
    result += 1

if C+1 <= W:
    result += 1
    
print(result)


