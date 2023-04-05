import sys
sys.stdin = open('4047.txt', 'r')

Test_case = int(input())

card_dict = {'S': 0, 'D': 1, 'H': 2, 'C': 3}

for t in range(Test_case):
    deck = [[0] * 14 for _ in range(4)]
    result = [13] * 4
    string = input()
    for c in range(0, len(string), 3):
        if deck[card_dict[string[c]]][int(''.join(map(str, string[c+1: c+3])))] != 0:
            result = 'ERROR'
            break

        else:
            deck[card_dict[string[c]]][int(''.join(map(str, string[c+1: c+3])))] += 1
    else:
        for i in range(4):
            result[i] -= sum(deck[i])

    print(f'#{t+1}', end=' ')

    if result == 'ERROR':
        print(result)
    else:
        print(*result)
