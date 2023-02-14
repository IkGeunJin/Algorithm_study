X, Y = map(int, input().split())

start, end = map(int, input().split())

time = int(input())

X_move = (start + time)
Y_move = (end + time)

if X_move // X % 2 == 0:
    ant_X = X_move % X
else:
    ant_X = X - (X_move % X)

if Y_move // Y % 2 == 0:
    ant_Y = Y_move % Y
else:
    ant_Y = Y - (Y_move % Y)

print(ant_X, ant_Y)