N = int(input())

result = 0
temp = 1
for n in range(1, N + 1):
    for i in range(1, n + 1):
        if n % i == 0:
            temp += 1
    result += (temp // 2)
    temp = 1

print(result)