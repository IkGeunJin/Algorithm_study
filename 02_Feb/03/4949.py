import sys
sys.stdin = open('4949_input.txt', 'r')

while True:                 # 입력의 마지막 조건으로 '.' 을 넣어준다고 되어있으므로 while 문 사용 및 '.' 입력 시 입력 종료
    string = input()        # while 문 반복 동안 문장을 string 에 할당
    temp = []               # 빈 리스트 (스택) 생성
    if string == '.':       # break 조건
        break
    for i in string:
        if i == '[':        # 여는 대괄호인 경우 스택에 추가
            temp.append(i)
        elif i == '(':      # 여는 소괄호인 경우 스택에 추가
            temp.append(i)
        elif i == ']':
            if '[' in temp and temp[-1] == '[':  # 닫는 대괄호인 경우 스택을 확인 후 스택의 마지막 값이 짝이 맞으면 스택 pop
                temp.pop()
            else:
                temp.append(i)  # 짝이 맞지 않은 경우 스택에 해당 문자열 추가 (for 문 종료 후 정답 조건) 후 break
                break
        elif i == ')':                            # 닫는 소괄호인 경우 스택을 확인 후 스택의 마지막 값이 짝이 맞으면 스택 pop
            if '(' in temp and temp[-1] == '(':
                temp.pop()
            else:
                temp.append(i)  # 짝이 맞지 않은 경우 스택에 해당 문자열 추가 (for 문 종료 후 정답 조건) 후 break
                break
    if len(temp) == 0:          # 짝이 다 맞은 경우 스택이 비어있으므로 'yes' 출력
        print('yes')
    else:                       # 짝이 맞지 않은 경우 스택이 비어있지않으므로 'no' 출력
        print('no')
