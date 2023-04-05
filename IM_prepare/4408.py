import sys
sys.stdin = open('4408.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    room = [0] * 401
    for _ in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        elif start == end:
            break
        if start % 2 == 0:
            start -= 1
        elif end % 2 == 1:
            end += 1
        for i in range(start, end + 1):
            room[i] += 1

    print(f'#{t+1} {max(room)}')
