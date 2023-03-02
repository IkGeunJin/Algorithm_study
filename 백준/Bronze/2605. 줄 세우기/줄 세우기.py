N = int(input())

line = list(map(int, input().split()))

stack = []

for i in range(N):
    stack.insert(i - line[i], i+1)

print(*stack)