from collections import deque
import sys

sys.stdin = open('2638.txt', 'r')


def find_out(si, sj):  # 외부 공기 찾는 함수
    queue = deque()    # BFS
    queue.append((si, sj))
    out[si][sj] = 3    # 모눈의 가장자리에는 치즈가 놓이지 않으므로 0,0 은 무조건 외부 공기
    # 치즈가 벽이라고 생각했을 때 이동할 수 있는 모든 구간을 외부 공간으로 표시한다.
    while queue:
        (ci, cj) = queue.popleft()
        for mi, mj in direction:
            ni, nj = ci + mi, cj + mj
            # 델타 탐색한 부분이 범위 내에 있으며, 치즈가 놓이지 않은 부분이라면 외부 표시
            if 0 <= ni < N and 0 <= nj < M and (out[ni][nj] == 0) and (board[ni][nj] == 0):
                out[ni][nj] = 3
                queue.append((ni, nj))


def melt(ci, cj):  # 외부 공기와 접촉한 치즈를 녹이는 함수
    count = 0
    if board[ci][cj] == 1:
        for mi, mj in direction:
            ni, nj = ci + mi, cj + mj
            if 0 <= ni < N and 0 <= nj < M and (out[ni][nj] == 3):  # 주변에 외부 공기와 닿는 부분이 몇 개인지 확인
                count += 1
            if count >= 2:  # 2개 이상일 경우
                board[ci][cj] = 0  # 해당 부분의 치즈를 녹인다.
                break


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

result = 0


while True:
    out = [[0] * M for _ in range(N)]  # 외부 공간 초기화

    find_out(0, 0)                     # 치즈를 기준으로 외부 공간 탐색

    for i in range(N):                 # 전체 치즈를 확인하여 외부 공간과 2변 이상이 접촉한 치즈를 녹인다
        for j in range(M):
            melt(i, j)

    result += 1                        # 녹을 경우 시간을 증가시킨다
    temp = 0                           # 치즈가 다 녹았는지 확인하기 위한 임시 변수
    for x in range(N):                 # 전체 Board 를 합산하여
        temp += sum(board[x])
    if temp == 0:                      # 0 이 나오면 치즈가 다 녹음
        break

print(result)
