A,B,C,X = map(int,input().split())
if B - A >= X and C  <= X:
    print(C / (B - A))
elif B - A >= X and C > X:
    print('1.000000000000')
else:
    print('0.000000000000')
    
