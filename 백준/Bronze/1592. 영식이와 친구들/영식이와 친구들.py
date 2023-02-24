N, M, L = map(int, input().split())

idx = 0
count = [0] * N
while True:
    count[idx] += 1
    if max(count) == M:
        break
    if count[idx] % 2 == 1:
        idx = (idx + L) % N
    else:
        idx = (idx - L) % N


print(sum(count) - 1)
