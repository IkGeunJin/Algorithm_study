Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    result = [[0] * (N + 1) for _ in range(N)]

    result[0][1] = 1

    for i in range(1, N):
        for j in range(1, N + 1):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    print(f'#{t+1}')
    for i in range(N):
        for j in range(N + 1):
            if result[i][j]:
                print(result[i][j], end=' ')
        print()
