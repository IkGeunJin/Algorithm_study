N = int(input())

num = list(map(int, input().split()))

stack = []
result = [-1]

for idx in range(N - 1, 0, -1):
    if num[idx-1] >= num[idx]:
        while True:
            if stack and stack[-1] <= num[idx-1]:
                stack.pop()
            else:
                if stack:
                    result.append(stack[-1])
                    break
                else:
                    result.append(-1)
                    break
    else:
        stack.append(num[idx])
        result.append(num[idx])

result = ' '.join(list(map(str, result[::-1])))

print(result)

