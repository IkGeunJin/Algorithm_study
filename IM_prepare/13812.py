import sys
sys.stdin = open('13812.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()
    bread = 0
    time = 0
    visit = 0
    while True:
        

    print(f'#{t+1} {result}')
