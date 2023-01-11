A,B = map(int,input().split())
x = B / A
print(f'{x:.3f}')
for i in range(4):
    print(f'{x:.{i}f}')

a = 123
b = 'abc'
print(f'{a} and {b}')

#右寄せ、中央寄せ、左寄せ
s = 'abc'
print(f'right : {s:*>8}')
print(f'center : {s:*^8}')
print(f'left  : {s:*<8}')

i = 1234567890
print(f'comma: {i:,}')

f = 0.123
print(f'percent: {f:.2%}')
# percent: 12.30%