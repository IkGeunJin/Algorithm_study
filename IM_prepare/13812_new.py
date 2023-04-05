import sys
sys.stdin = open('13812.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()
    time = 0
    result = 'Possible'
    for a in arrive:
        time += 1
        if time > (a//M)*K:
            result = 'Impossible'
            break

    print(f'#{t+1} {result}')
