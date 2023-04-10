S = input()  # 文字列Sを入力する
n = len(S)
ans = ""

# Sの2i-1文字目と2i文字目を入れ替える
for i in range(n // 2):
    ans += S[2*i+1]
    ans += S[2*i]

print(ans)
