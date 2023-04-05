import sys
sys.stdin = open('A.txt', 'r')

Test_case = int(input())


def check(idx_i, idx_j):
    for move_i, move_j in direction:
        current_i, current_j = idx_i + move_i, idx_j + move_j
        while True:
            current_i += move_i
            current_j += move_j
            if (0 <= current_i < N) and (0 <= current_j < N) and cell[current_i][current_j] == 0:
                cell[current_i][current_j] = 1
            elif cell[current_i][current_j] == 1:
                while True:
                    current_i -= move_i
                    current_j -= move_j
                    if (current_i, current_j) == (idx_i, idx_j):
                        break
                    cell[current_i][current_j] = 0
                if (current_i, current_j) == (idx_i, idx_j):
                    break
        else:
            break


for t in range(1):
    N = int(input())
    cell = [list(map(int, input().split())) for _ in range(N)]
    core = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if cell[i][j] == 1:
                core.append((i, j))

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    check(core[0][0], core[0][1])

    for n in range(N):
        print(cell[n])