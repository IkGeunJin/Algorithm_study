def bfs(start):
    visited[start] = 1
    queue = [start]

    while queue:
        s = queue.pop(0)
        for e in route[s]:
            if visited[e] == 0:
                visited[e] = visited[s] + node_map[(s, e)]
                queue.append(e)


N, M = map(int, input().split())

node_map = {}
route = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    node1, node2, distance = map(int, input().split())
    route[node1].append(node2)
    route[node2].append(node1)
    node_map[(node1, node2)] = distance
    node_map[(node2, node1)] = distance

for _ in range(M):
    visited = [0] * (N + 1)
    A, B = tuple(map(int, input().split()))
    bfs(A)
    print(visited[B] - 1)