paper_g, paper_s = map(int, input().split())      # 종이의 가로, 세로 입력

cut = int(input())                                # 자르는 횟수 입력

g_list = [0]                                      # 자르고 난 후 index 확인을 위하여 0이 들어있는 빈 List 생성
s_list = [0]
for c in range(cut):                              # 자르는 횟수만큼 반복
    gs, num = map(int, input().split())           # 가로, 세로 여부 및 커팅라인 인덱스 입력
    if gs == 1:                                   # 1 인 경우 가로로 자른다
        g_list.append(num)                        # 가로 커팅라인 리스트에 입력
    else:                                         # 0 인 경우 세로로 자른다
        s_list.append(num)                        # 세로 커팅라인 리스트에 입력

g_list.append(paper_g)                            # 종이의 끝부분 index 확인을 위하여 리스트에 추가
s_list.append(paper_s)

g_list = sorted(g_list)                           # 자르는 위치가 정렬되어 입력되지 않으므로 자른 후 정렬
s_list = sorted(s_list)

g_result = []                                     # 결과값 입력을 위한 리스트 생성
for i in range(1, len(g_list)):                   # 0, 커팅라인, 종이 끝단이 입력된 리스트를 바탕으로
    g_result.append(g_list[i] - g_list[i-1])      # 각 커팅라인에서 자르고 남은 부분의 길이를 결과 List 에 담는다

s_result = []
for j in range(1, len(s_list)):
    s_result.append(s_list[j] - s_list[j-1])

print(max(g_result) * max(s_result))               # 최대 크기를 출력하는 문제이므로 남은 부분이 가장 긴 부분끼리 곱하여 결과 출력
