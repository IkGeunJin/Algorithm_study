paper_g, paper_s = map(int, input().split())

cut = int(input())

g_list = [0]
s_list = [0]
for c in range(cut):
    gs, num = map(int, input().split())
    if gs == 1:
        g_list.append(num)
    else:
        s_list.append(num)

g_list.append(paper_g)
s_list.append(paper_s)

g_list = sorted(g_list)
s_list = sorted(s_list)

g_result = []
for i in range(1, len(g_list)):
    g_result.append(g_list[i] - g_list[i-1])

s_result = []
for j in range(1, len(s_list)):
    s_result.append(s_list[j] - s_list[j-1])

print(max(g_result) * max(s_result))