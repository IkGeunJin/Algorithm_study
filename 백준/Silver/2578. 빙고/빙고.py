board = [list(map(int, input().split())) for _ in range(5)]

num = [list(map(int, input().split())) for _ in range(5)]

MC = []
for m in range(5):
    for n in range(5):
        MC.append(num[m][n])

bingo = []

for i in range(5):
    temp1 = []
    temp2 = []
    for j in range(5):
        temp1.append(board[i][j])
        temp2.append(board[j][i])
    bingo.append(temp1)
    bingo.append(temp2)

temp1 = []
temp2 = []
for i in range(5):
    temp1.append(board[i][i])
    temp2.append(board[i][4-i])
bingo.append(temp1)
bingo.append(temp2)

count = 0
for i in range(25):
    for j in range(5):
        for k in range(12):
            if MC[i] == bingo[k][j]:
                bingo[k][j] = 0
    if bingo.count([0] * 5) >= 3:
        count = i + 1
        break

print(count)