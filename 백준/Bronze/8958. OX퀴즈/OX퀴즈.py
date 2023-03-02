Test_case = int(input())

for t in range(Test_case):
    quiz = input()
    score = 0
    result = 0
    for q in quiz:
        if q == 'O':
            score += 1
            result += score
        else:
            score = 0

    print(result)
