Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    num = list(map(int, input().split()))
    temp = []
    for i in range(N):
        for j in range(N):
            if i == j:        # i와 j가 같은 경우는 없으므로 연산을 하지 않음
                continue
            else:             # temp 에 모든 경우의 곱 연산 결과를 삽입
                temp.append(num[i] * num[j])
    temp = sorted(list(set(temp)))[::-1]   # set 으로 중복 제거 및 다시 리스트로 바꿔 정렬

    result = -1   # 단조 증가하는 수가 없는 경우 결과는 -1 이므로 -1로 초기값 설정

    for i in range(len(temp)):   # 전체 temp 에 들어있는 값들을 검사
        temp[i] = str(temp[i])   # str 으로 변환 시 각 인덱스를 슬라이싱하여 검사 가능 (리스트 변환 불필요, 유니코드 사용)
        for j in range(1, len(temp[i])):   # temp 내의 인자들을 슬라이싱하여 검사
            if temp[i][j] < temp[i][j-1]:
                temp[i] = 0   # 단조 증가하지 않는 부분이 있으면 해당 인자를 0으로 만들고 반복문 종료 (불필요한 반복 방지)
                break
        if temp[i]:           # 0 이 아닌 경우
            result = int(temp[i])   # 다시 int로 변환 후 result 에 할당, 반복문 종료 (내림차순으로 정렬하였으므로 가장 큰 수 이다.)
            break

    print(f'#{t+1} {result}')
