N = int(input())
dasom = int(input())
temp = []
result = 0

for _ in range(N - 1):
    M = int(input())
    temp.append(M)

while temp:
    if dasom > max(temp):
        break
    temp.sort()
    temp[-1] -= 1
    dasom += 1
    result += 1

print(result)