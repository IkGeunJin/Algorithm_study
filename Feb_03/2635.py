num = int(input())

count = 1
result = []
second_num = 62
while True:
    if num < 0 or second_num < 0:
        break
    num = num - second_num
    second_num = second_num - num
    count += 1
    result.append(num)
    result.append(second_num)

print(count)
print(result)