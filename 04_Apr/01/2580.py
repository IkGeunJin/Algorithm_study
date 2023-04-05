import sys
sys.stdin = open('2580.txt', 'r')

input = sys.stdin.readline


def check_i(tj, num):
    for a in range(9):
        if num == board[a][tj]:
            return 0
    return 1


def check_j(ti, num):
    for a in range(9):
        if num == board[ti][a]:
            return 0
    return 1


def check_s(ti, tj, num):
    si = ti // 3 * 3
    sj = tj // 3 * 3
    for a in range(3):
        for b in range(3):
            if num == board[si+a][sj+b]:
                return 0
    return 1


board = [list(map(int, input().split())) for _ in range(9)]

blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

flag = False


def dfs(s):
    global flag

    if flag:
        return

    if s == len(blank):
        for output in range(9):
            print(*board[output])
        flag = True
        return 0

    for n in range(1, 10):
        ni = blank[s][0]
        nj = blank[s][1]

        if check_i(nj, n) and check_j(ni, n) and check_s(ni, nj, n):
            board[ni][nj] = n
            dfs(s + 1)
            board[ni][nj] = 0


dfs(0)
