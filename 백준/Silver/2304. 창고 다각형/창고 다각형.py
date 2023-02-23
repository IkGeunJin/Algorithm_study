import sys

N = int(sys.stdin.readline())

garage = [0] * 1001

for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    garage[L] = H

front = 0
front_idx = 0
for i in range(len(garage)):
    if garage[i] > front:
        front = garage[i]
        front_idx = i
        break

rear = 0
rear_idx = 0
for j in range(len(garage) - 1, -1, -1):
    if garage[j] > rear:
        rear = garage[j]
        rear_idx = j
        break

garage = garage[front_idx: rear_idx + 1]

if front > rear:
    garage = garage[::-1]

top = max(garage)

count = 0
while True:
    top = max(garage)
    if max(garage) == 0:
        break
    while True:
        if garage[0] <= 0:
            garage.pop(0)
        else:
            break

    if garage[0] == top:
        garage = garage[::-1]
        if garage[0] == garage[-1]:
            count += len(garage) * garage[0]
            break

    count += len(garage) * garage[0]
    minus = garage.pop(0)
    for j in range(len(garage)):
        garage[j] -= minus

print(count)
