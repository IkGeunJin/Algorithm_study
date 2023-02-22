#  삼각파 공식
#  x는 실행 정수, A는 진폭, P는 주기/2, y는 결과값
#  y = (A/P) * (P - abs(x % (2*P) - P))

#  해당 문제에서는 (1, 1) 씩 움직이므로 진폭 == 주기
#  진폭, 주기는 격자 공간 크기
#  실행 정수 x는 시작 위치 + 시간
#  최종 위치가 y이다.

X, Y = map(int, input().split())

start_X, start_Y = map(int, input().split())

time = int(input())

start_X += time
start_Y += time

end_X = int((X/X) * (X - abs(start_X % (2*X) - X)))
end_Y = int((Y/Y) * (Y - abs(start_Y % (2*Y) - Y)))

print(end_X, end_Y)