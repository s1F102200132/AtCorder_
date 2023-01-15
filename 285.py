a,b = map(int,input().split())
flag = False
if a == 1 and b == 2:
    flag = True
if a == 1 and b == 3:
    flag = True
if a == 2 and b == 4:
    flag = True
if a == 2 and b == 5:
    flag = True
if a == 4 and b == 8:
    flag = True
if a == 4 and b == 9:
    flag =True
if a == 5 and b == 10:
    flag = True
if a == 5 and b == 11:
    flag = True
if a == 3 and b == 6:
    flag = True
if a == 3 and b == 7:
    flag = True
if a == 6 and b == 12:
    flag = True
if a == 6 and b == 13:
    flag = True
if a == 7 and b == 14:
    flag = True
if a == 7 and b == 15:
    flag = True


print('Yes' if flag == True else 'No')