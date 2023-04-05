Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    bus_stop = [0] * 1001
    result = 0
    for _ in range(N):
        bus_type, start, end = map(int, input().split())
        for i in range(start, end + 1):
            if bus_type == 1:
                bus_stop[i] += 1
            else:
                bus_stop[start] += 1
                bus_stop[end] += 1
                break
        for j in range(start + 1, end):
            if bus_type == 2:
                if start % 2 == 0:
                    if j % 2 == 0:
                        bus_stop[j] += 1
                else:
                    if j % 2 == 1:
                        bus_stop[j] += 1
            elif bus_type == 3:
                if start % 2 == 0:
                    if j % 4 == 0:
                        bus_stop[j] += 1
                else:
                    if j % 3 == 0 and j % 10 != 0:
                        bus_stop[j] += 1

    print(f'#{t+1} {max(bus_stop)}')
