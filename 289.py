s = input()
print(s.replace('0', 'x').replace('1', '0').replace('x', '1'))

s = input()
 
for i in s:
    if i == '0':
        print('1', end = '')
    else:
        print('0', end = '')