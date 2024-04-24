import sys
input = sys.stdin.readline

N = int(input())
balls = {}
ballNum = {}
for i in range(N):          # 색깔, 크기
    color, size = map(int, input().split())
    balls[color] = balls.get(color, []) + [size]
    ballNum[i+1] = [color, size]
# print(balls)
# print(ballNum)
for i in range(N):
    tmp = 0
    color = ballNum[i+1][0]
    size = ballNum[i+1][1]
    for key, value in balls.items():
        if key != color:
            for v in value:
                if v < size:
                    tmp += v
    print(tmp)