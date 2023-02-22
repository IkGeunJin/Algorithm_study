num = int(input())

temp = [num]

case_list = []
for i in range(num+1):
    temp.append(i)
    idx = 0
    while True:
        n = temp[idx] - temp[idx+1]
        temp.append(n)
        idx += 1
        if n < 0:
            temp.pop()
            break
    case_list.append(temp)
    temp = [num]

result = 0
for j in range(len(case_list)):
    if len(case_list[j]) > result:
        result = len(case_list[j])
        result_list = case_list[j]

print(result)
print(*result_list)