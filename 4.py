def isAC(i): 
    if i[0] != 'A':
        return False
    elif i[1:-1].count('C') != 1:
        return False
    if sum(map(str.isupper,i)) != 2:
        return False
    return True
print('AC' if isAC(input())else 'WA')

