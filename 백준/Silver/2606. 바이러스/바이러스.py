def dfs(start):
    visited = [0] * (V + 1)
    stack = []

    s = start
    visited[s] = 1

    while True:
        for e in route[s]:
            if visited[e] == 0:
                stack.append(s)

                s = e
                visited[s] = 1
                result.append(s)
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break


result = []

V = int(input())
E = int(input())
route = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    route[start].append(end)
    route[end].append(start)

dfs(1)

print(len(result))
