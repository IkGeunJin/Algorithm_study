N, M = map(int, input().split())

card = list(map(int, input().split()))

jack = []
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if i == j or i == k or j == k:
                continue
            jack.append(card[i]+card[j]+card[k])

black = 0
for i in range(len(jack)):
    if black <= jack[i] <= M:
        black = jack[i]

print(black)