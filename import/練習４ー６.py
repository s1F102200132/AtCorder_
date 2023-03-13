#前の二つの要素を足した数値が次の要素になるようにnumberに追加していくただし、1000を超過しないようにする
numbers = [1,1]
result = sum(numbers)
count = 2
while result <= 1000:
    numbers.append(result)
    result +=  numbers[count - 1]
    count += 1
print(numbers)

#要素の値÷1つ前の要素値を要素とした新しいリストradioを作成
radio = []
for i in range(1,len(numbers)):
    radio.append(numbers[i] / numbers[i-1])
print(radio)

#小数点３位までの値にする
for j in range(len(numbers)-1):
    radio[j] = int(radio[j] * 1000) / 1000
print(radio)