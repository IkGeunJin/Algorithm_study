king, rock, N = input().split()
king, rock, N = list(king), list(rock), int(N)
king[1], rock[1] = int(king[1]), int(rock[1])

moving_data = {'R': (1, 0),
               'L': (-1, 0),
               'B': (0, -1),
               'T': (0, 1),
               'RT': (1, 1),
               'LT': (-1, 1),
               'RB': (1, -1),
               'LB': (-1, -1)
               }

for _ in range(N):
    move = input()
    king_x, king_y = chr(ord(king[0]) + moving_data[move][0]), king[1] + moving_data[move][1]
    if 'A' <= king_x <= 'H' and 1 <= king_y <= 8:
        if [king_x, king_y] == rock:
            rock_x, rock_y = chr(ord(rock[0]) + moving_data[move][0]), rock[1] + moving_data[move][1]
            if 'A' <= rock_x <= 'H' and 1 <= rock_y <= 8:
                rock = [rock_x, rock_y]
            else:
                continue
        king = [king_x, king_y]
    else:
        continue

print(''.join(map(str, king)))
print(''.join(map(str, rock)))
