X, Y = map(int, input().split())

start, end = map(int, input().split())

time = int(input())

direction_x = [1, -1]
direction_y = [1, -1]

idx_x = 0
idx_y = 0
for _ in range(time):
    start = start + direction_x[idx_x]
    end = end + direction_y[idx_y]
    if start == 0 or start == X:
        idx_x = (idx_x + 1) % 2
    if end == 0 or end == Y:
        idx_y = (idx_y + 1) % 2

print(start, end)