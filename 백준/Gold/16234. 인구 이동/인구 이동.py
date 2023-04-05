def bfs(start_i, start_j):
    queue = [(start_i, start_j)]
    visited[start_i][start_j] = 1
    temp = [(start_i, start_j)]
    while queue:
        current_i, current_j = queue.pop(0)
        for move_i, move_j in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            next_i, next_j = current_i + move_i, current_j + move_j
            if (0 <= next_i < N) and (0 <= next_j < N) and (visited[next_i][next_j] == 0) and (L <= abs(country[next_i][next_j] - country[current_i][current_j]) <= R):
                queue.append((next_i, next_j))
                temp.append((next_i, next_j))
                visited[next_i][next_j] = 1

    return temp


N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
result = 0

while True:
    flag = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                idx = bfs(i, j)
                if len(idx) > 1:
                    flag = 1
                    count = 0
                    for a, b in idx:
                        count += country[a][b]
                    for a, b in idx:
                        country[a][b] = count // len(idx)

    if flag == 0:
        break
    result += 1

print(result)
