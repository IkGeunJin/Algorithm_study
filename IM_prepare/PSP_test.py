import sys
sys.stdin = open('PSP.txt', 'r')
sys.setrecursionlimit(10**8)


def pop_(start_i, start_j):
    global flower
    flower += balloons[start_i][start_j]
    visited[start_i][start_j] = 1
    for r in range(1, balloons[start_i][start_j] + 1):
        for move_i, move_j in direction:
            next_i, next_j = start_i + (move_i * r), start_j + (move_j * r)
            if (0 <= next_i < N) and (0 <= next_j < M) and (visited[next_i][next_j] == 0):
                pop_(next_i, next_j)


Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[0] * M for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            flower = 0
            pop_(i, j)
            if result < flower:
                result = flower

    print(result)