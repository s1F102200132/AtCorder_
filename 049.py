s = input()

while len(s) > 0:
    if s.endswith('dreamer'):
        s = s[:-7]  # 'dreamer'の部分を削除
    elif s.endswith('dream'):
        s = s[:-5]  # 'dream'の部分を削除
    elif s.endswith('eraser'):
        s = s[:-6]  # 'eraser'の部分を削除
    elif s.endswith('erase'):
        s = s[:-5]  # 'erase'の部分を削除
    else:
        print('NO')
        break

if len(s) == 0:
    print('YES')
