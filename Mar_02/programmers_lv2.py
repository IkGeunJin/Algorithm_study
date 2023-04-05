# 서비스 가입자 늘리기
# 판매액 늘리기

# n 명의 카톡 사용자 이모티콘 m 개 할인 판매
# 할인율 10%, 20%, 30%, 40%

# 자신의 기준에 따라 일정 비율 이상 할인 모두 구매
# 이모티콘 구매 비용의 합이 일정 가격 이상이 되면 구매 모두 취소 후 이모티콘 플러스 가입

def solution(users, emoticons):
    max_cost = 0
    max_percent = 0
    for u in range(len(users)):
        if max_cost < users[u][1]:
            max_cost = users[u][1]
        if max_percent < users[u][0]:
            max_percent = users[u][0]

    for e in range(len(emoticons)):
        emoticons[e] = max_percent * emoticons / 100

    count = 0
    result = 0
    for i in range(len(users)):
        if users[i][1] < sum(emoticons):
            count += 1
        else:
            result += sum(emoticons)

    answer = [result, emoticons]

    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))