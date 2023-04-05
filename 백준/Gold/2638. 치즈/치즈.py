from collections import deque
import sys


def find_out(si, sj):
    queue = deque()
    queue.append((si, sj))
    out[si][sj] = 3

    while queue:
        (ci, cj) = queue.popleft()
        for mi, mj in direction:
            ni, nj = ci + mi, cj + mj
            if 0 <= ni < N and 0 <= nj < M and (out[ni][nj] == 0) and (board[ni][nj] == 0):
                out[ni][nj] = 3
                queue.append((ni, nj))


def melt(ci, cj):
    count = 0
    if board[ci][cj] == 1:
        for mi, mj in direction:
            ni, nj = ci + mi, cj + mj
            if 0 <= ni < N and 0 <= nj < M and (out[ni][nj] == 3):
                count += 1
            if count >= 2:
                board[ci][cj] = 0
                break


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

result = 0


while True:
    out = [[0] * M for _ in range(N)]

    find_out(0, 0)

    for i in range(N):
        for j in range(M):
            melt(i, j)

    result += 1
    temp = 0
    for x in range(N):
        temp += sum(board[x])
    if temp == 0:
        break

print(result)
