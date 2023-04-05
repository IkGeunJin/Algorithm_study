N = int(input())

candy = [list(input()) for _ in range(N)]
result = []


def change(si, sj):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for mi, mj in direction:
        ni, nj = si + mi, sj + mj
        if 0 <= ni < N and 0 <= nj < N and candy[ni][nj] != candy[si][sj]:
            candy[si][sj], candy[ni][nj] = candy[ni][nj], candy[si][sj]
            for a in range(N):
                temp = 1
                for b in range(1, N):
                    if candy[a][b] == candy[a][b - 1]:
                        temp += 1
                result.append(temp)

            for b in range(N):
                temp = 1
                for a in range(1, N):
                    if candy[a - 1][b] == candy[a][b]:
                        temp += 1
                result.append(temp)
            candy[si][sj], candy[ni][nj] = candy[ni][nj], candy[si][sj]


for i in range(N):
    count = 1
    for j in range(1, N):
        if candy[i][j] == candy[i][j - 1]:
            count += 1
    result.append(count)

for j in range(N):
    count = 1
    for i in range(1, N):
        if candy[i - 1][j] == candy[i][j]:
            count += 1
    result.append(count)

for i in range(N):
    for j in range(N):
        change(i, j)

print(max(result))
