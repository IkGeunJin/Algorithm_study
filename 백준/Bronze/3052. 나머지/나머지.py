numbers = 10

result = []
for _ in range(numbers):
    N = int(input())
    result.append(N % 42)

print(len(set(result)))