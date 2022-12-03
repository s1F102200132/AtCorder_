S = list(input())
result = 0
for i in S:
    if i == 'v':
        result += 1
    elif i == 'w':
        result += 2
print(result)