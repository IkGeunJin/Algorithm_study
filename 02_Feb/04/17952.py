import sys

N = int(sys.stdin.readline())    # 입력을 빨리 받는 방법 (백준에서는 대부분 활용하면 좋음)

stack = []                       # 선입후출 방식을 사용하기 위해 빈 스택 생성
result = 0                       # 결과값 0으로 선언
for n in range(N):               # N 분 동안 과제를 진행
    Temp = list(map(int, sys.stdin.readline().split()))   # 리스트로 전체를 받은 후 판단
    if Temp[0]:                  # 맨 앞이 0이 아니면 과제를 받은 것이므로
        A, T = Temp[1], Temp[2]  # 과제 점수와 과제를 하는데 걸리는 시간을 할당
        stack.append(A)          # 점수, 시간을 순차적으로 스택에 삽입
        stack.append(T - 1)      # 과제를 받은 즉시 과제를 시작한다고 하였으니 남은 시간은 -1하여 삽입
    else:
        if stack:                # 맨 앞이 0이라면 과제를 받지 않았음
            stack[-1] -= 1       # 해당 시간에는 하던 과제를 진행하니까 시간 -1

    if stack and stack[-1] == 0:  # 스택을 확인했을 때 스택에 가장 마지막 값이 0이면 과제를 다 했다는 뜻
        stack.pop()               # 시간을 pop 하고
        result += stack.pop()     # 과제의 점수를 pop 한 후 result 에 더해준다.
    else:
        continue

print(result)