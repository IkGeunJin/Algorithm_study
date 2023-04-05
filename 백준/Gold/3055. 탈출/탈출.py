import sys
from collections import deque
import copy

input = sys.stdin.readline


def b_bfs():
    global flag

    while bq:
        bci, bcj = bq.popleft()
        for di, dj in directions:
            bni, bnj = bci + di, bcj + dj
            if 0 <= bni < R and 0 <= bnj < C:
                if vb[bni][bnj] == 0 and tdd[bni][bnj] == '.':
                    vb[bni][bnj] = 1
                    bt.append((bni, bnj))
                if tdd[bni][bnj] == 'D':
                    flag = 1


def w_bfs():

    while wq:
        wci, wcj = wq.popleft()
        for di, dj in directions:
            wni, wnj = wci + di, wcj + dj
            if 0 <= wni < R and 0 <= wnj < C:
                if vw[wni][wnj] == 0 and tdd[wni][wnj] == '.':
                    vw[wni][wnj] = 1
                    wt.append((wni, wnj))
                    tdd[wni][wnj] = '*'


R, C = map(int, input().split())

tdd = [list(input()) for _ in range(R)]
dg = ws = bs = 0

vb = [[0] * C for _ in range(R)]
vw = [[0] * C for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count = 0
bq = deque()
bt = deque()
wq = deque()
wt = deque()
result = 'KAKTUS'
flag = 0

for i in range(R):
    for j in range(C):
        if tdd[i][j] == 'D':
            dg = (i, j)
        elif tdd[i][j] == '*':
            ws = (i, j)
            vw[i][j] = 1
            wq.append((i, j))
        elif tdd[i][j] == 'S':
            bs = (i, j)
            vb[i][j] = 1
            bq.append((i, j))

while True:
    w_bfs()
    b_bfs()
    wq = wt.copy()
    bq = bt.copy()
    wt = deque()
    bt = deque()
    count += 1
    if flag == 1:
        result = count
        break
    if len(wq) == 0 and len(bq) == 0:
        break

print(result)
