string = input()
tag_idx = []
temp = []

if '<' in string:
    string += '<'
    string = '>' + string
    for i in range(len(string)):
        if string[i] == '<' or string[i] == '>':
            tag_idx.append(i)

    for j in range(len(tag_idx)-1):
        temp.append(string[tag_idx[j]:tag_idx[j+1]+1])

    for k in range(len(temp)):
        if temp[k][0] == '>' and temp[k][-1] == '<':
            temp[k] = temp[k][1:-1]
            temp[k] = temp[k].split()
            for x in range(len(temp[k])):
                temp[k][x] = temp[k][x][::-1]
            temp[k] = ' '.join(temp[k])

    result = ''.join(temp)

else:
    temp = string.split(' ')
    for x in range(len(temp)):
        temp[x] = temp[x][::-1]
    result = ' '.join(temp)

print(result)
