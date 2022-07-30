def slime():
    A,B,K = map(int,input().split())
    num = A
    result = 0
    while not (num >= B):
        result += 1
        num *= K
    return result
print(slime())

