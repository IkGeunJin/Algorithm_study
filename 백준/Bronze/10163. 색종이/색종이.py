import sys

N = int(sys.stdin.readline())

paper = [[0] * 1001 for _ in range(1001)]

for n in range(1, N + 1):
    start_i, start_j, length_i, length_j = map(int, sys.stdin.readline().split())
    for i in range(start_i, start_i + length_i):
        for j in range(start_j, start_j + length_j):
            paper[i][j] = n


for n in range(1, N + 1):
    count = 0
    for i in range(1001):
        count += paper[i].count(n)
    print(count)
