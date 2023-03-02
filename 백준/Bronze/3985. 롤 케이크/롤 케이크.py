L = int(input())
N = int(input())

cake = [0] * (L + 1)
want = [0] * (N + 1)
real = [0] * (N + 1)

for n in range(1, N + 1):
    P, K = map(int, input().split())
    want[n] = (K - P + 1)
    for i in range(P, K + 1):
        if cake[i] == 0:
            cake[i] = n
            real[n] += 1

temp = 0
for i in range(len(want)):
    if temp < want[i]:
        temp = want[i]
        result1 = i

result2 = real.index(max(real))

print(result1)
print(result2)
