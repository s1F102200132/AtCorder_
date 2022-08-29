A,B,C,D,E = map(int,input().split())
result = []
res = []
list = [A,B,C,D,E]
def re():
    for i in list:
        if i == list[0]:
            result.append(i)
        if len(res) > 0  and result[0] != i  :
            if i ==res[0]:
                res.append(i)
            else:
                return 'No'
    return 'Yes'
print(res(1,2,1,2,1))