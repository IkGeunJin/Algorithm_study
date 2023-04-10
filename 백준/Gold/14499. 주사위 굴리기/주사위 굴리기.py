import sys
from copy import deepcopy

# 위 서 동 북 남 아래
# 기본
# 1 4 3 2 5 6
# 동
# 4 6 1 2 5 3
# 서
# 3 1 6 2 5 4
# 북
# 5 4 3 1 6 2
# 남
# 2 4 3 6 1 5


def turn(n):
    global dice
    temp = [0] * 6
    if n == 1:
        temp[0], temp[1], temp[2], temp[3], temp[4], temp[5] = dice[1], dice[5], dice[0], dice[3], dice[4], dice[2]
    elif n == 2:
        temp[0], temp[1], temp[2], temp[3], temp[4], temp[5] = dice[2], dice[0], dice[5], dice[3], dice[4], dice[1]
    elif n == 3:
        temp[0], temp[1], temp[2], temp[3], temp[4], temp[5] = dice[4], dice[1], dice[2], dice[0], dice[5], dice[3]
    elif n == 4:
        temp[0], temp[1], temp[2], temp[3], temp[4], temp[5] = dice[3], dice[1], dice[2], dice[5], dice[0], dice[4]
    dice = deepcopy(temp)


N, M, x, y, K = map(int, input().split())

direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

dice = [0] * 6

arr = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))

for i in range(K):
    idx = move[i] - 1
    if 0 <= x + direction[idx][0] < N and 0 <= y + direction[idx][1] < M:
        x += direction[idx][0]
        y += direction[idx][1]
        turn(move[i])
        print(dice[0])
        if arr[x][y] == 0:
            arr[x][y] = dice[5]
        else:
            dice[5] = arr[x][y]
            arr[x][y] = 0
    else:
        continue
