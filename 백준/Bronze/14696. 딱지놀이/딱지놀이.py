N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    game_A = [0] * 5
    game_B = [0] * 5
    for a in range(1, len(A)):
        game_A[A[a]] += 1

    for b in range(1, len(B)):
        game_B[B[b]] += 1

    result = 'D'
    for i in range(4, -1, -1):
        if game_A[i] > game_B[i]:
            result = 'A'
            break
        elif game_A[i] < game_B[i]:
            result = 'B'
            break
        else:
            continue

    print(result)
