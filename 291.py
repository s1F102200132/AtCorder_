s = input() # 入力文字列を取得する
for i in range(len(s)):
    if s[i].isupper(): # 文字列の i 番目の文字が大文字かどうかを確認する
        print(i+1) # 大文字が先頭から何文字目にあるかを出力する
        break
