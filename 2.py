Z = int(input())
X,Y = map(int,input().split())
exist = False
for i in range (X,Y+1):
    if i % Z == 0:
        exist == True
print('OK'if exist else 'NG')

