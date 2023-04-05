import sys
sys.stdin = open('16811.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    result = N
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            if carrot[i] != carrot[i + 1] and carrot[j] != carrot[j + 1]:
                S = len(carrot[0: i + 1])
                M = len(carrot[i + 1: j + 1])
                L = len(carrot[j + 1: N])
                if S * M * L != 0 and max(S, M, L) <= N // 2:
                    if result > (max(S, M, L) - min(S, M, L)):
                        result = (max(S, M, L) - min(S, M, L))

    if result == N:
        result = -1

    print(f'#{t+1} {result}')
