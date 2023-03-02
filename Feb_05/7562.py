def bfs(i, j):
    queue = [[i, j]]
    visited[i][j] = 1

    while queue:
        current_i, current_j = queue.pop(0)
        for move_i, move_j in direction:
            next_i, next_j = current_i + move_i, current_j + move_j
            if (0 <= next_i < N) and (0 <= next_j < N) and visited[next_i][next_j] == 0:
                visited[next_i][next_j] = visited[current_i][current_j] + 1
                queue.append([next_i, next_j])
            if (next_i, next_j) == (end_i, end_j):
                break


Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    start_i, start_j = map(int, input().split())
    end_i, end_j = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    direction = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    bfs(start_i, start_j)

    print(visited[end_i][end_j] - 1)