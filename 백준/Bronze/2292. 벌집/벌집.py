N = int(input())

room = 1
count = 1
while N > room:
    if N == 1:
        break
    room += (6 * count)
    count += 1

print(count)
