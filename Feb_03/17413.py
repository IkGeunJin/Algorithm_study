string = input()
tag_idx = []
temp = []

if '<' in string:
    # tag 가 문자열 내에 있는 경우
    string = '>' + string + '<'
    # 문자열 앞 뒤를 tag 로 감싸준다
    for i in range(len(string)):
        if string[i] == '<' or string[i] == '>':
            tag_idx.append(i)
    # 문자열 내의 tag 의 인덱스를 tag_idx 에 넣어준다

    for j in range(len(tag_idx)-1):
        temp.append(string[tag_idx[j]:tag_idx[j+1]+1])
    # tag 를 기준으로 문자열을 쪼개서 temp 에 넣어준다

    for k in range(len(temp)):
        # temp 내에서 '>' 와 '<' 로 감싸진 요소는 tag 로 감싸지지 않은 문자열
        if temp[k][0] == '>' and temp[k][-1] == '<':
            temp[k] = temp[k][1:-1]
            # '>' 와 '<' 슬라이싱으로 제거
            temp[k] = temp[k].split()
            # 띄어쓰기를 기준으로 나눠서 리스트에 넣는다
            for x in range(len(temp[k])):
                temp[k][x] = temp[k][x][::-1]
                # 리스트 내의 요소들을 하나씩 뒤집는다
            temp[k] = ' '.join(temp[k])
            # 다시 string 타입으로 띄어쓰기하여 합치기

    result = ''.join(temp)
    # 전체 리스트를 string 으로 합치기

else:
    # 문자열 내에 tag 가 없는 경우
    temp = string.split(' ')
    for x in range(len(temp)):
        temp[x] = temp[x][::-1]
    result = ' '.join(temp)

print(result)