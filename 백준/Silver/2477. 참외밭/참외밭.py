K = int(input())

temp1 = []
temp2 = []
total = []

for i in range(6):
    _, length = map(int, input().split())
    total.append(length)
    if i % 2 == 0:
        temp1.append(length)
    else:
        temp2.append(length)

ns = total.index(max(temp1))
we = total.index(max(temp2))

result = total[ns] * total[we] - (total[ns - 3] * total[we - 3])

result *= K

print(result)
