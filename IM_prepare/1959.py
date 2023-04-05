import sys
sys.stdin = open('1959.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A

    result = 0
    for i in range(M - N + 1):
        temp = 0
        for j in range(N):
            temp += A[j] * B[i+j]
        if temp > result:
            result = temp

    print(f'#{t+1} {result}')
