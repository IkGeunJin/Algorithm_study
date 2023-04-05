import sys
input = sys.stdin.readline


def check_col(ti, num):
    for a in range(9):
        if board[ti][a] == num:
            return False
    return True


def check_row(tj, num):
    for a in range(9):
        if board[a][tj] == num:
            return False
    return True


def check_box(ti, tj, num):
    bi = (ti // 3) * 3
    bj = (tj // 3) * 3
    for a in range(bi, bi+3):
        for b in range(bj, bj+3):
            if board[a][b] == num:
                return False
    return True


def sdk(n):
    if n == k:
        for output in range(9):
            print(*board[output])
        exit(0)

    ti = key[n][0]
    tj = key[n][1]
    for check in range(1, 10):
        if check_col(ti, check) and check_row(tj, check) and check_box(ti, tj, check):
            board[ti][tj] = check
            sdk(n+1)
            board[ti][tj] = 0


board = [list(map(int, input().split())) for _ in range(9)]
key = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            key.append((i, j))

k = len(key)

sdk(0)
