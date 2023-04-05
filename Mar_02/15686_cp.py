import sys
import itertools


def ch_dt(h, c):  # 치킨 거리를 구하기 위한 함수
    distance = abs(h[0] - c[0]) + abs(h[1] - c[1])
    return distance


N, M = map(int, sys.stdin.readline().split())

city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

home = []  # 집들의 위치를 받기 위한 빈 리스트 생성
chicken = []  # 치킨집의 위치를 받기 위한 빈 리스트 생성
live = []  # 폐업하지 않는 치킨집을 고르기 위한 빈 리스트 생성

for i in range(N):  # 2차원 리스트 전체를 순회하며
    for j in range(N):
        if city[i][j] == 1:  # 1 인 경우 home 에 좌표를 tuple 로 삽입
            home.append((i, j))
        elif city[i][j] == 2:  # 2 인 경우 chicken 에 좌표를 tuple 로 삽입
            chicken.append((i, j))

live = list(itertools.combinations(chicken, M))  # itertools 의 combinations 를 활용한 전체 치킨집 중 M 개를 고른다

result = 10000  # 최대값 선언 : 50개의 집에서 가장 멀다고 가정한 경우 100 의 거리가 나오므로 (50 + 50) 최댓값은 5000 이다
for i in live:  # 전체 치킨집 중 골라낸 M개의 치킨집의 경우들을 순회
    count = 0
    for j in home:  # 전체 집들의 경우에서
        temp = 100  # 최대값 선언 : 1개의 집에서 가장 멀리 있을 수 있는 치킨집의 거리는 100 이므로 최댓값은 100 이다
        for k in range(M):  # M 개의 치킨집 중 가장 가까이 있는 치킨집의 거리를 ch_dt 로 찾는다
            if temp > ch_dt(i[k], j):  # 최소값을 찾아
                temp = ch_dt(i[k], j)  # temp 에 넣어준 후
        count += temp  # 이 값들을 count 변수에 넣어준다
    if result > count:  # 각 경우들을 순회하며 최소값을 찾아 이를 result 에 넣어준다
        result = count

print(result)
