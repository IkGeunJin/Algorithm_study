import sys

N, M = map(int, sys.stdin.readline().split())  # 총 나무 수, 필요한 나무
tree = list(map(int, sys.stdin.readline().split()))  # 나무를 list 로 입력 받는다

start = 0
end = max(tree)  # 끝 점을 가장 높은 나무로 잡는다

# 이진 탐색
while start <= end:  # 시작 점이 끝 점보다 작은 동안 (최대값을 구해야 함, middle 값에서 정확히 잘리지 않는 케이스도 존재)
    middle = (start + end) // 2  # 탐색 값은 시작과 끝 점의 중간 지점
    cut = 0  # 잘린 나무 합
    for t in tree:
        if t > middle:  # 현재 탐색 값보다 큰 나무는 잘림
            cut += (t - middle)

    if cut >= M:  # 원하는 나무보다 더 많이 잘랐다면
        start = middle + 1  # 시작 점을 당겨온다 (탐색 값이 커질수록 잘리는 나무는 적어짐)
    else:          # 원하는 나무보다 덜 잘랐다면
        end = middle - 1  # 끝 점을 당겨온다 (탐색 값이 작아질수록 잘리는 나무는 커짐)

print(end)
