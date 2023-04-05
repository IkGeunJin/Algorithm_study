N = int(input())  # 수열의 크기 정수 N

num = list(map(int, input().split()))  # 수열 입력

stack = []     # 빈 스택 생성
result = [-1]  # 수열의 마지막 수는 무조건 -1이므로 -1을 넣고 시작

for idx in range(N - 1, 0, -1):  # 수열을 거꾸로 검사
    if num[idx-1] >= num[idx]:   # 바로 앞의 수가 현재 idx 보다 큰 경우
        while True:              # 뒤의 수들 중에서 오큰수를 찾아야 한다.
            if stack and stack[-1] <= num[idx-1]:  # 스택이 비어 있지 않고 top 이 앞의 수보다 작을 경우
                stack.pop()      # 스택을 pop 한다
            else:                # 스택이 비어 있거나 top 이 더 큰 경우
                if stack:        # top 이 더 큰 경우
                    result.append(stack[-1])  # 해당 숫자가 오큰수이므로 결과에 삽입
                    break                     # while 문 반복 종료
                else:            # 스택이 비어 있는 경우
                    result.append(-1)  # 해당 숫자는 오큰수가 없으므로 -1 삽입
                    break
    else:                        # 바로 앞의 수가 현재 idx 보다 작은 경우
        stack.append(num[idx])   # 현재 idx 가 오큰수이므로 스택 및 결과에 삽입
        result.append(num[idx])

result = ' '.join(list(map(str, result[::-1])))   # 뒤집어서 검사하였으므로 다시 뒤집어서 출력

print(result)

