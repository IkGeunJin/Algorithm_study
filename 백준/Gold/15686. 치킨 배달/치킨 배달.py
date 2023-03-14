import sys
import itertools


def ch_dt(h, c):
    r = abs(h[0] - c[0]) + abs(h[1] - c[1])
    return r


N, M = map(int, sys.stdin.readline().split())

city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

home = []
chicken = []
live = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

live = list(itertools.combinations(chicken, M))

result = 10000
for i in live:
    count = 0
    for j in home:
        temp = 100
        for k in range(M):
            if temp > ch_dt(i[k], j):
                temp = ch_dt(i[k], j)
        count += temp
    if result > count:
        result = count

print(result)
