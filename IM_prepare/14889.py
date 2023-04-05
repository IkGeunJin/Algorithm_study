import sys

N = int(sys.stdin.readline())

team = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

temp = []
link = []
result = []

for i in range(N):
    for j in range(N):
        if i != j:
            temp.append(team[i][j] + team[j][i])

for i in range(len(temp) // 2):
    result.append(abs(temp[i] - temp[len(temp) - i - 1]))

print(temp)
print(result)