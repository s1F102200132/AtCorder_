n = int(input())
h = list(map(int, input().split()))
i = h.index(max(h))
print(i + 1)
#index()リストの要素のインデックス（何番目か）を取得