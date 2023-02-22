while True:
    string = input()
    temp = []
    if string == '.':
        break
    for i in string:
        if i == '[':
            temp.append(i)
        elif i == '(':
            temp.append(i)
        elif i == ']':
            if '[' in temp and temp[-1] == '[':
                temp.pop()
            else:
                temp.append(i)
                break
        elif i == ')':
            if '(' in temp and temp[-1] == '(':
                temp.pop()
            else:
                temp.append(i)
                break
    if len(temp) == 0:
        print('yes')
    else:
        print('no')