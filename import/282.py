K = int(input())
for i in range(K):
    print(chr(ord('A') + i),end ='')

#文字をUnicodeコードポイントに変換: ord()
#Unicodeコードポイントを文字に変換: chr()