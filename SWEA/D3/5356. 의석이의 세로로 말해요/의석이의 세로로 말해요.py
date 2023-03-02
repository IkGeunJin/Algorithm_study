Test_case = int(input())

for t in range(Test_case):
    string = [list(input()) for _ in range(5)]
    max_length = 0
    result = ''
    for i in range(5):
        if max_length < len(string[i]):
            max_length = len(string[i])

    while True:
        for i in range(5):
            if len(string[i]) < max_length:
                string[i].append('')
                break
        else:
            break

    for j in range(max_length):
        for i in range(5):
            result += string[i][j]

    print(f'#{t+1} {result}')
