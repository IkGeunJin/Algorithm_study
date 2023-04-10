import sys
from collections import deque


def bfs1(si, sj):
    global tsi, tsj, fuel
    pt = []
    q = deque()
    q.append((si, sj))
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    if arr[si][sj] > 1:
        pt.append((si, sj, visited[si][sj]))

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni, nj))
                    if arr[ni][nj] > 1:
                        pt.append((ni, nj, visited[ni][nj]))

    if not pt:
        return -1
    else:
        pt.sort(key=lambda x: (x[2], x[0], x[1]))
        tsi = pt[0][0]
        tsj = pt[0][1]
        fuel = fuel - (visited[tsi][tsj] - 1)
        return fuel


def bfs2(si, sj, ei, ej):
    global tsi, tsj, fuel
    q = deque()
    q.append((si, sj))
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1

    if si == ei and sj == ej:
        tsi, tsj = si, sj
        return

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni, nj))
                    if ni == ei and nj == ej:
                        tsi, tsj = ni, nj
                        if fuel - (visited[ni][nj] - 1) <= -1:
                            fuel = -1
                        else:
                            fuel = fuel + (visited[ni][nj] - 1)
                        return
    fuel = -1
    return


N, M, fuel = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

tsi, tsj = map(int, input().split())
tsi -= 1
tsj -= 1

temp = 2
route = {}
for m in range(M):
    psi, psj, pei, pej = map(int, input().split())
    arr[psi - 1][psj - 1] = temp
    route[temp] = (pei - 1, pej - 1)
    temp += 1

temp_i = temp_j = 0
cnt = 0
while True:
    a = bfs1(tsi, tsj)
    if a <= -1:
        result = -1
        break
    else:
        temp_i, temp_j = tsi, tsj
        tei, tej = route[arr[tsi][tsj]]
        arr[temp_i][temp_j] = 0
        bfs2(tsi, tsj, tei, tej)
        if fuel <= -1:
            result = -1
            break
    cnt += 1

    if cnt == M:
        result = fuel
        break

print(result)
