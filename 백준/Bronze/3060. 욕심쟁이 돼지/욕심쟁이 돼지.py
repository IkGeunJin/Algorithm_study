Test_case = int(input())

for _ in range(Test_case):
    N = int(input())
    pig = list(map(int, input().split()))
    eat = [0] * 6

    count = 1
    while True:
        if sum(pig) > N:
            break
        for i in range(6):
            eat[i] = pig[i] + pig[i - 1] + pig[(i + 1) % 6] + pig[(i + 3) % 6]
        pig = eat[:]
        count += 1

    print(count)
