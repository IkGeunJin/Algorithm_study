H, W = map(int, input().split())
block = list(map(int, input().split()))
block_left = 0
block_right = W - 1

rain = []

# while True:
#     if block_left == block_right:
#         break
for i in range(1, W):
    # if block_left != 0 and block[block_left] == max(block):
    #     break
    if block[block_left] <= block[i]:
        if i <= block_left:
            continue
        else:
            for rain_left in range(block_left, i):
                rain.append(block[block_left] - block[rain_left])
            block_left = i

if not block_left == block_right:
    for k in range(W - 1, -1, -1):
        # if block_right != W - 1 and block[block_right] == max(block):
        #     break
        if block_left == block_right:
            break
        if block[block_right] <= block[k]:
            if k >= block_right:
                continue
            else:
                for rain_right in range(block_right, k, -1):
                    rain.append(block[block_right] - block[rain_right])
                block_right = k

print(sum(rain))