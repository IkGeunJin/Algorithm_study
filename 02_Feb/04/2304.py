import sys
sys.stdin = open('2304_input.txt', 'r')

N = int(sys.stdin.readline())

garage = [0] * 1001  # L 의 maximum 이 1000 이므로 1001 길이의 빈 리스트 생성

for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    garage[L] = H  # L 위치의 인덱스에 높이 H 입력

front = 0  # 맨 앞에 나오는 숫자가 front
front_idx = 0  # 그 인덱스도 저장하기 위한 변수 할당
for i in range(len(garage)):
    if garage[i] > front:  # 0이 나오다가 더 큰 수가 나오면 front
        front = garage[i]
        front_idx = i
        break

rear = 0
rear_idx = 0
for j in range(len(garage) - 1, -1, -1):  # 반대로 오면서 동일하게 rear 를 찾음
    if garage[j] > rear:
        rear = garage[j]
        rear_idx = j
        break

garage = garage[front_idx: rear_idx + 1]  # 앞 뒤로 0 을 다 제거한 리스트로 변환

if front > rear:  # 리스트를 기준으로 앞이 더 크면 뒤집어준다 (작은 값이 앞으로)
    garage = garage[::-1]

count = 0  # 넓이 값을 넣어줄  count 변수 생성
while True:
    top = max(garage)  # 가장 높은 지점을 top 에 할당
    if max(garage) <= 0:  # top 이 0 보다 작거나 같다면 break
        break
    while True:  # 반복문 순회 중 front 가 0 이하가 아닐때까지 pop(0)
        if garage[0] <= 0:
            garage.pop(0)
        else:
            break

    if garage[0] == top or garage[0] > garage[-1]:  # 맨 앞이 top 이거나 맨 뒤보다 높아지면 뒤집어준다.
        garage = garage[::-1]
        if garage[0] == garage[-1]:  # 맨 앞과 맨 뒤가 모두 top 이면
            count += len(garage) * garage[0]  # 맨 앞에서 뒤까지의 면적을 넣어주고 break
            break

    count += len(garage) * garage[0]  # 맨 앞부분의 높이부터 전체 너비만큼 곱해서 면적을 구하여 count 에 더해준다.
    minus = garage.pop(0)  # 맨 앞부분을 pop 하여 나온 높이를 minus 변수에 할당하고
    for j in range(len(garage)):  # 전체 리스트에서 minus 만큼 빼준다.
        garage[j] -= minus

print(count)
