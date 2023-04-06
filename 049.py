from copy import deepcopy

# 爆弾の爆発範囲内のマスを更新する関数
def update_board(board, r, c, power):
    for i in range(-power, power+1):
        for j in range(-power, power+1):
            if abs(i) + abs(j) <= power:
                x, y = r+i, c+j
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    board[x][y] = "."

# 盤面の状態を出力する関数
def print_board(board):
    for row in board:
        print("".join(row))

# 盤面の入力
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

# 盤面のコピーを取る
new_board = deepcopy(board)

# 爆弾の座標を取得し、爆破範囲を更新する
for r in range(R):
    for c in range(C):
        if board[r][c] != "." and board[r][c] != "#":
            power = int(board[r][c])
            update_board(new_board, r, c, power)

# 爆破後の盤面を出力する
print_board(new_board)
