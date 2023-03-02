N, K = map(int, input().split())

room = [[0] * 7, [0] * 7]
for _ in range(N):
    S, Y = map(int, input().split())
    room[S][Y] += 1

result = 0
for i in range(2):
    for j in range(7):
        if room[i][j] % K == 0:
            result += room[i][j] // K
        else:
            result += room[i][j] // K + 1

print(result)