import sys
sys.stdin = open('2805_input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    middle = N // 2     # 행렬의 중앙 부분
    garden = [list(map(int, input())) for _ in range(N)]
    start = N // 2      # 시작과 끝 모두 중앙에서 시작해서
    end = N // 2
    count = 0
    for i in range(N):
        for j in range(start, end+1):  # i 를 기준으로 두고
            count += garden[i][j]  # count 에 해당 범위의 값들을 더해준다.
        if i < middle:   # i 가 middle 보다 작은 경우 간격을 넓히다가
            start -= 1
            end += 1
        else:            # i 가 middle 과 같은 순간부터 끝까지 간격을 좁혀준다.
            start += 1
            end -= 1

    print(f'#{t+1} {count}')
