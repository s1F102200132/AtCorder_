#入力例
#3 4
#..#
#.#
#.#
#出力例
#1 2 0 
H,W = map(int,input().split())
count_list = [0] * W
for i in range(H):
    C = list(str(input()))
    for j in range(W):
        if C[j] == '#':
            count_list[j] += 1
print(*count_list)
