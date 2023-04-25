import sys

outcome = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]


def check(v, s):
    global board
    global result
    temp = []
    if v == 5:
        if sum(sum(board, [])) == 0:
            result = 1
            return
    elif s == 6:
        check(v+1, v+2)
    else:
        if board[v][0] != 0 and board[s][2] != 0:
            temp.append([0, 2])
        if board[v][1] != 0 and board[s][1] != 0:
            temp.append([1, 1])
        if board[v][2] != 0 and board[s][0] != 0:
            temp.append([2, 0])
        for a, b in temp:
            board[v][a] -= 1
            board[s][b] -= 1
            check(v, s+1)
            board[v][a] += 1
            board[s][b] += 1


case = 4
for c in range(case):
    board = []
    for j in range(6):
        board.append(outcome[c][3*j:3*j+3])
    result = 0
    check(0, 1)
    if c != 3:
        print(result, end=' ')
    else:
        print(result)
