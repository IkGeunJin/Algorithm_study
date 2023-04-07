from collections import deque
import sys
import copy
input = sys.stdin.readline


def bfs():
    global safe
    q = deque()
    temp = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                q.append((i, j))

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if temp[ni][nj] == 0:
                    temp[ni][nj] = 2
                    q.append((ni, nj))

    count = 0
    for bi in range(N):
        for bj in range(M):
            if temp[bi][bj] == 0:
                count += 1
    safe = max(safe, count)


def btk(wall):
    if wall == 3:
        bfs()
        return

    for ti in range(N):
        for tj in range(M):
            if arr[ti][tj] == 0:
                arr[ti][tj] = 1
                btk(wall+1)
                arr[ti][tj] = 0


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

safe = 0
btk(0)
print(safe)
