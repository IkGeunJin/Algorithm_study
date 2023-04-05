import sys
sys.stdin = open('1979.txt')

Test_case = int(input())

for t in range(Test_case):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                count += 1
                if count == K and j == (N - 1):
                    result += 1
            else:
                if count == K:
                    result += 1
                count = 0

    for j in range(N):
        count = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                count += 1
                if count == K and i == (N - 1):
                    result += 1
            else:
                if count == K:
                    result += 1
                count = 0

    print(f'#{t+1} {result}')
