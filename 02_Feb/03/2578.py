board = [list(map(int, input().split())) for _ in range(5)]

num = [list(map(int, input().split())) for _ in range(5)]

MC = []

for m in range(5):
    for n in range(5):
        MC.append(num[m][n])  # 사회자가 부르는 순서를 1차원 리스트로 변경

bingo = []

for i in range(5):
    temp1 = []
    temp2 = []
    for j in range(5):
        temp1.append(board[i][j])  # 세로줄 빙고 케이스
        temp2.append(board[j][i])  # 가로줄 빙고 케이스
    bingo.append(temp1)
    bingo.append(temp2)

temp1 = []
temp2 = []
for i in range(5):
    temp1.append(board[i][i])  # 대각선 빙고 케이스
    temp2.append(board[i][4-i])  # 반대편 대각선 빙고 케이스
bingo.append(temp1)
bingo.append(temp2)

count = 0
for i in range(25):  # 사회자가 1개씩 부름
    for j in range(5):  # 빙고 케이스 가로
        for k in range(12):  # 빙고 케이스 세로
            if MC[i] == bingo[k][j]:
                bingo[k][j] = 0  # 사회자가 부르는 번호 0으로 지우기
    if bingo.count([0] * 5) >= 3:  # 0이 5개면 빙고, 빙고줄이 3개가 넘는 순간
        count = i + 1  # 사회자가 0번 불렀을 때 1이므로 i + 1을 카운트에 넣고
        break  # 반복문 break

print(count)