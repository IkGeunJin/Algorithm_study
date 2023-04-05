from collections import deque
import sys
import copy

sys.stdin = open('15686.txt', 'r')


def bfs(start_i, start_j):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append([start_i, start_j])
    visited[start_i][start_j] = 1
    mv = 0
    sv = 0

    while q:
        current_i, current_j = q.popleft()
        for move_i, move_j in direction:
            next_i, next_j = current_i + move_i, current_j + move_j
            if 0 <= next_i < N and 0 <= next_j < N and (visited[next_i][next_j] == 0):
                q.append([next_i, next_j])
                visited[next_i][next_j] = visited[current_i][current_j] + 1
                if city[next_i][next_j] == 1:
                    sv += visited[next_i][next_j] - 1
                    if mv == 0:
                        mv = visited[next_i][next_j] - 1
    return [mv, sv, start_i, start_j]


def bfs_2(case, start_i, start_j):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append([start_i, start_j])
    visited[start_i][start_j] = 1

    while q:
        current_i, current_j = q.popleft()
        for move_i, move_j in direction:
            next_i, next_j = current_i + move_i, current_j + move_j
            if 0 <= next_i < N and 0 <= next_j < N and (visited[next_i][next_j] == 0):
                q.append([next_i, next_j])
                visited[next_i][next_j] = visited[current_i][current_j] + 1
                if case[next_i][next_j] == 2:
                    return visited[next_i][next_j] - 1


N, M = map(int, sys.stdin.readline().split())

city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
city_1 = copy.deepcopy(city)
city_2 = copy.deepcopy(city)

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

temp_1 = []
temp_2 = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            temp = bfs(i, j)
            temp_1.append(temp)
            temp_2.append(temp)

temp_1.sort(key=lambda x: x[0])
temp_1.sort(key=lambda x: x[1])

temp_2.sort(key=lambda x: x[1])
temp_2.sort(key=lambda x: x[0])

while True:
    if len(temp_1) == M and len(temp_2) == M:
        break
    delete_1 = temp_1.pop()
    city_1[delete_1[2]][delete_1[3]] = 0
    delete_2 = temp_2.pop()
    city_2[delete_2[2]][delete_2[3]] = 0

print(temp_1)
print(temp_2)

result_1 = []
result_2 = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            result_1.append(bfs_2(city_1, i, j))
            result_2.append(bfs_2(city_2, i, j))

print(min(sum(result_1), sum(result_2)))
