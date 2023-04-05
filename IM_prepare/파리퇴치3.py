import sys
sys.stdin = open('파리퇴치3.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    direction_1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    direction_2 = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    result = 0

    for i in range(N):
        for j in range(N):
            catch = 0
            catch += fly[i][j]
            for move_i, move_j in direction_1:
                for m in range(1, M):
                    current_i, current_j = i + (move_i * m), j + (move_j * m)
                    if 0 <= current_i < N and 0 <= current_j < N:
                        catch += fly[current_i][current_j]
            if result < catch:
                result = catch
            catch = 0
            catch += fly[i][j]
            for move_i, move_j in direction_2:
                for m in range(1, M):
                    current_i, current_j = i + (move_i * m), j + (move_j * m)
                    if 0 <= current_i < N and 0 <= current_j < N:
                        catch += fly[current_i][current_j]
            if result < catch:
                result = catch

    print(f'#{t+1} {result}')
