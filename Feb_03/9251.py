string_1 = input()
string_2 = input()

sub_set_1 = []
sub_set_2 = []

total_1 = []
total_2 = []

result = []

for i in range(1 << len(string_1)):
    sub_set_1 = []
    for j in range(len(string_1)):
        if i & (1 << j):
            sub_set_1.append(string_1[j])
    total_1.append(sub_set_1)

for i in range(1 << len(string_2)):
    sub_set_2 = []
    for j in range(len(string_2)):
        if i & (1 << j):
            sub_set_2.append(string_2[j])
    total_2.append(sub_set_2)

for i in range(len(total_1)):
    for j in range(len(total_2)):
        if total_1[i] == total_2[j]:
            result.append(total_1[i])

Answer = 0
for i in range(len(result)):
    if Answer < len(result[i]):
        Answer = len(result[i])

print(Answer)