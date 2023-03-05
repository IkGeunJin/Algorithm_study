N, K = map(int, input().split())

wheel = ['?'] * N
idx = 0

for _ in range(K):
    change, alphabet = input().split()
    change = int(change)
    idx = (idx + change) % N
    if wheel[idx] == '?':
        if alphabet in wheel:
            wheel = '!'
            break
        else:
            wheel[idx] = alphabet
    elif wheel[idx] == alphabet:
        continue
    else:
        wheel = '!'
        break
else:
    wheel = wheel[::-1]
    while True:
        if wheel[0] == alphabet:
            wheel = ''.join(wheel)
            break
        wheel.append(wheel.pop(0))

print(wheel)
