for i in range(9):
    for j in range(9):
        print('{} X {} = {}'.format(i+1,j+1,((i+1)*(j+1))))
#奇数の段のみ計算
for i in range(9):
    if (i+1) % 2 == 0:
        continue
    for j in range(9):
        print('{} X {} = {}'.format(i+1,j+1,((i+1)*(j+1))))
#50を超えたら次の段へ
for i in range(9):
    if (i+1) % 2 == 0:
        continue
    for j in range(9):
        if (i+1) * (j + 1) > 50:
            break
        print('{} X {} = {}'.format(i+1,j+1,((i+1)*(j+1))))

