N = int(input())

room = 6
count = 1
while N > 1:
    N -= room
    count += 1
    room += 6

print(count)
