conference = int(input())
conference_list = []

for c in range(conference):
    start, end = map(int, input().split())
    conference_list.append((start, end))

result = [0]
for i in range(len(conference_list)):
    temp = conference_list[i]
    idx = i + 1
    count = 1
    while True:
        if idx <= max(result):
            break
        if temp[1] < conference_list[idx][0]:
            temp = conference_list[idx]
            count += 1
        else:
            idx += 1
    result.append(count)

print(max(result))