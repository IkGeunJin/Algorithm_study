num = int(input())       # 입력 받은 수를 num 에 넣고

temp = [num]             # 리스트의 0번 인덱스에 num 넣어서 만듬

case_list = []           # 전체 case 다 탐색해서 List 에 넣음
for i in range(num+1):   # num 자기자신도 뺄 수 있음
    temp.append(i)       # 반례 : 1 입력 시 4, 1 1 0 1 나와야하는데 3, 1 0 1 나옴
    idx = 0              # while 문 반복 시 마다 idx 값 초기화
    while True:
        n = temp[idx] - temp[idx+1]    # 리스트의 0번 인덱스에서 1번 인덱스를 뺀 후
        temp.append(n)                 # 해당 값을 temp 에 넣어준다
        idx += 1                       # 이후 인덱스를 1 증가시켜 1번 인덱스에서 2번 인덱스를 뺄 수 있게끔 설정
        if n < 0:                      # while 문 break 조건 (음의 정수가 나올 경우 break)
            temp.pop()                 # 음의 정수도 append 된 이후이므로 pop 을 통하여 제거
            break
    case_list.append(temp)             # 해당 case 가 다 들어있는 temp 를 case_list 에 넣은 후
    temp = [num]                       # temp 초기화

result = 0
for j in range(len(case_list)):        # case_list 내의 전체 리스트들을 범위로 지정
    if len(case_list[j]) > result:     # list 길이가 가장 긴 리스트를 result 에 넣고
        result = len(case_list[j])     # 해당 리스트를 결과 리스트에 넣어준다
        result_list = case_list[j]

print(result)
print(*result_list)