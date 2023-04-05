import sys
sys.stdin = open('1220.txt', 'r')

Test_case = 10

for t in range(Test_case):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    temp = [[] for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if i > j:
                table[i][j], table[j][i] = table[j][i], table[i][j]

    count = 0
    for a in range(100):
        for b in range(100):
            if table[a][b]:
                if table[a][b] == 2:
                    table[a][b] = 0
                else:
                    break

    for a in range(100):
        for b in range(99, -1, -1):
            if table[a][b]:
                if table[a][b] == 1:
                    table[a][b] = 0
                else:
                    break

    for a in range(100):
        for b in range(100):
            if table[a][b]:
                temp[a].append(table[a][b])

    count = 0
    for i in range(100):
        for j in range(1, len(temp[i])):
            if temp[i][j - 1] == 1 and temp[i][j] == 2:
                count += 1

    print(f'#{t+1} {count}')
