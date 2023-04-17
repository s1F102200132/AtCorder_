N = int(input())
W = list(input().split())
flag = False
for i in W:
    if i == 'and'or i=='not'or i == 'that' or i =='the' or i == 'you':
        flag = True
print('Yes' if flag else 'No')
