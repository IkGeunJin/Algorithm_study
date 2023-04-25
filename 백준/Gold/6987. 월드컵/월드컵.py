import sys

outcome = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]


#  경기하는 경우의 수 [0 ~ 4, 1 ~ 5]
def check(v, s):
    global board
    global result
    temp = []  # 경기하는 두 팀의 결과를 담기 위한 temp 선언
    if v == 5:  # 백트래킹 종료 조건
        if sum(sum(board, [])) == 0:  # 모든 상황을 다 깔끔하게 소모했다면
            result = 1  # 1을 넣어두고
            return  # 함수 종료
    elif s == 6:  # v가 5번까지와의 경기를 다 끝냈다면
        check(v+1, v+2)  # v를 1 더해서 다음 경기 진행
    else:
        if board[v][0] and board[s][2]:  # v가 승리 가능하고 s에 패배가 남아있다면
            temp.append([0, 2])
        if board[v][1] and board[s][1]:  # 둘 다 무승부가 남아있다면
            temp.append([1, 1])
        if board[v][2] and board[s][0]:  # v가 패배 s가 승리 가능 시
            temp.append([2, 0])
        for a, b in temp:  # temp 에 넣어둔 경우의 수를 바탕으로 승, 무, 패 카운트 -1
            board[v][a] -= 1
            board[s][b] -= 1
            check(v, s+1)  # dfs 실시
            board[v][a] += 1  # 원상복구
            board[s][b] += 1


case = 4
for c in range(case):
    board = []
    for j in range(6):
        board.append(outcome[c][3*j:3*j+3])  # 3칸 씩 잘라서 board 에 넣어둔다
    result = 0
    check(0, 1)
    if c != 3:
        print(result, end=' ')
    else:
        print(result)
