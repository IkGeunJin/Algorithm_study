import sys
sys.stdin = open('13732.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    left_i = N
    left_j = N
    right_i = 0
    right_j = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                if left_i > i:
                    left_i = i
                if left_j > j:
                    left_j = j
                if right_i <= i:
                    right_i = i
                if right_j <= j:
                    right_j = j

    if right_i - left_i == right_j - left_j:
        result = 'yes'
    else:
        result = 'no'

    for i in range(left_i, right_i + 1):
        for j in range(left_j, right_j + 1):
            if arr[i][j] == '.':
                result = 'no'
                break

    print(f'#{t+1} {result}')
