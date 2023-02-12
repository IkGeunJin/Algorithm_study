import sys
sys.stdin = open('input.txt', 'r')

while True:
    string = input()
    result = 'yes'
    temp = []
    if string == '.':
        break
    for i in string:
        if i == '[':
            temp.append(i)
        elif i == '(':
            temp.append(i)
        elif i == ']':
            if '[' in temp:
                if temp[-1] == '[':
                    temp.pop()
                else:
                    result = 'no'
                    break
            else:
                result = 'no'
                break
        elif i == ')':
            if '(' in temp:
                if temp[-1] == '(':
                    temp.pop()
                else:
                    result = 'no'
                    break
            else:
                result = 'no'
                break
    print(result)