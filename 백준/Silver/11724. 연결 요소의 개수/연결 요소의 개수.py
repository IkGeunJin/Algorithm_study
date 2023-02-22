# 6 0 의 경우 노드는 6개이나 간선이 없으므로 output = 6 이 나와야한다

import sys  # readline 안하면 시간초과

V, E = map(int, sys.stdin.readline().split())  # 정점, 간선 입력
route = [[] for _ in range(V+1)]  # 연결 데이터를 위한 리스트 생성
count = 1  # visited 에 방문 표시를 할 때 다른 연결 요소는 다른 숫자로 표현하기 위해 count 변수 선언
visited = [-1] + [0] * V  # 0 번 노드는 없기 때문에 겹치지 않기 위해 -1 이 입력된 방문 리스트 생성

for _ in range(E):  # 간선의 수 만큼 반복
    node1, node2 = map(int, sys.stdin.readline().split())
    route[node1].append(node2)  # 양방향으로 연결 상태 데이터 입력
    route[node2].append(node1)

for v in range(1, V + 1):  # 간선이 없더라도 1개의 노드는 1개의 연결 상태를 가지므로 연결 상태에 본인도 넣어둔다
    route[v].append(v)


for s in range(1, V + 1):  # 1번 노드부터 마지막 노드까지 확인을 위한 반복
    stack = []  # 빈 스택 생성
    if visited[s] == 0:  # 방문하지 않았을 경우에만 방문 표시 (조건문 달지 않으면 무조건 방문표시를 해버림)
        visited[s] = count  # 1 대신 카운트 변수를 통한 표시
        while True:
            for e in route[s]:  # s 에서 갈 수 있는 모든 e의 경우에서 (본인은 방문표시를 했으므로 무시)
                if visited[e] == 0:  # 방문하지 않았다면
                    stack.append(s)  # 막힌 경우 돌아오기 위해 스택에 넣어두고
                    visited[e] = count  # count 변수를 통한 방문 표시 후
                    s = e  # 출발점 재설정
            else:  # 모든 경우를 다 방문한 경우
                if stack:  # 다른 경우가 있을 때 까지 스택을 pop 한다.
                    stack.pop()
                else:  # 스택이 다 비워진 경우
                    count += 1  # count 변수에 1을 더한 후 (다른 연결 요소 구분을 위함)
                    break  # while 문 종료하고 2번 노드부터 끝까지 반복
    else:
        continue
    

print(len(set(visited))-1)  # set 으로 중복을 제거하여 연결 요소의 수량 확인 (0의 경우 -1을 채워뒀기 때문에 -1 해준다)
