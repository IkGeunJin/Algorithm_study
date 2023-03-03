Block_X, Block_Y = map(int, input().split())

N = int(input())

store = []
result = []
for _ in range(N):
    way, distance = map(int, input().split())
    store.append((way, distance))

DG_way, distance = map(int, input().split())

for i in store:
    if DG_way == 1:
        if i[0] == 1:
            result.append(abs(distance - i[1]))
        elif i[0] == 2:
            left = distance + Block_Y + i[1]
            right = (Block_X - distance) + Block_Y + (Block_X - i[1])
            result.append(min(left, right))
        elif i[0] == 3:
            result.append(distance + i[1])
        else:
            result.append(Block_X - distance + i[1])

    elif DG_way == 2:
        if i[0] == 1:
            left = distance + Block_Y + i[1]
            right = (Block_X - distance) + Block_Y + (Block_X - i[1])
            result.append(min(left, right))
        elif i[0] == 2:
            result.append(abs(distance - i[1]))
        elif i[0] == 3:
            result.append(distance + Block_Y - i[1])
        else:
            result.append(Block_X - distance + Block_Y - i[1])

    elif DG_way == 3:
        if i[0] == 1:
            result.append(distance + i[1])
        elif i[0] == 2:
            result.append(Block_Y - distance + i[1])
        elif i[0] == 3:
            result.append(abs(distance - i[1]))
        else:
            left = distance + Block_X + i[1]
            right = (Block_Y - distance) + Block_X + (Block_Y - i[1])
            result.append(min(left, right))

    else:
        if i[0] == 1:
            result.append(distance + Block_X - i[1])
        elif i[0] == 2:
            result.append(Block_Y - distance + Block_X - i[1])
        elif i[0] == 3:
            left = (Block_Y - distance) + Block_X + (Block_Y - i[1])
            right = distance + Block_X + i[1]
            result.append(min(left, right))
        else:
            result.append(abs(distance - i[1]))

print(sum(result))
