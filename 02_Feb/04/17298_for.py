# For 문 활용해서 쉽게 풀었으나 시간 초과

N = int(input())

num = list(map(int, input().split()))

for i in range(N):
    result = 0
    if i == (N-1):
        print(-1)
        break
    elif max(num[i+1:]) > num[i]:
        for j in range(i+1, N):
            if num[j] > num[i]:
                result = num[j]
                break
    else:
        result = -1
    print(result, end=' ')

