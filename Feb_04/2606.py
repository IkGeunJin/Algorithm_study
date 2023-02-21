def dfs(point):  # dfs 함수 선언
    visited = [0] * (V + 1)  # 재방문 방지를 위해 방문 확인용 리스트 생성
    stack = []  # 빈 스택 생성

    s = point  # dfs 함수 사용 시 출발 지점을 s 에 할당
    visited[s] = 1  # 출발 지점 방문 처리

    while True:
        for e in route[s]:  # s 와 연결된 e 중
            if visited[e] == 0:  # 방문하지 않은 node 가 있는 경우
                stack.append(s)  # 다시 돌아올 지점을 stack 에 넣어주고

                s = e  # 다시 출발 위치를 현 위치로 변경 후
                visited[s] = 1  # 방문 처리
                result.append(s)  # 결과에 삽입
                break
        else:  # 방문하지 않은 node 가 없는 경우
            if stack:  # 스택이 비어있지 않으면
                s = stack.pop()  # 돌아갈 위치까지 stack 을 pop 한다
            else:  # 스택이 비어있다면 모든 경우를 다 확인하였으므로
                break  # while 문 break


result = []  # 결과 리스트 생성

V = int(input())
E = int(input())
route = [[] for _ in range(V + 1)]  # 각 node 간의 연결 데이터를 담을 리스트 생성

for _ in range(E):
    start, end = map(int, input().split())  # 양방향 연결
    route[start].append(end)
    route[end].append(start)

# 낮은 숫자을 우선한다는 내용이 있다면 정렬을 통하여 낮은 숫자 먼저 확인 필요
# for i in range(len(route)):
#     route[i].sort()

dfs(1)

print(len(result))  # 출발 지점은 result 에 담지 않아, 1번을 제외한 나머지 출력
