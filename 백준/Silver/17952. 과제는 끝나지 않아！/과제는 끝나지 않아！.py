import sys

N = int(sys.stdin.readline())

stack = []
result = 0
for n in range(N):
    Temp = list(map(int, sys.stdin.readline().split()))
    if Temp[0]:
        A, T = Temp[1], Temp[2]
        stack.append(A)
        stack.append(T - 1)
    else:
        if stack:
            stack[-1] -= 1

    if stack and stack[-1] == 0:
        stack.pop()
        result += stack.pop()
    else:
        continue

print(result)
