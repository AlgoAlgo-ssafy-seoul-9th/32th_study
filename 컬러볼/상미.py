# import sys
# input = sys.stdin.readline

# N = int(input())
# balls = {}
# ballNum = {}
# for i in range(N):          # 색깔, 크기
#     color, size = map(int, input().split())
#     balls[color] = balls.get(color, []) + [size]
#     ballNum[i+1] = [color, size]
# # print(balls)
# # print(ballNum)
# for i in range(N):
#     tmp = 0
#     color = ballNum[i+1][0]
#     size = ballNum[i+1][1]
#     for key, value in balls.items():
#         if key != color:
#             for v in value:
#                 if v < size:
#                     tmp += v
#     print(tmp)


import sys
input = sys.stdin.readline

N = int(input())
balls = []
for i in range(N):
    C, S = map(int, input().split())
    balls.append((C, S, i))

balls.sort(key=lambda x: x[1])
results = [0] * N

# 색상별 합과 전체 합을 계산
color_sum = {}
total_sum = 0
j = 0  # 이전에 살펴본 위치

# 각 공들을 차례로 보면서
for i in range(N):
    while balls[j][1] < balls[i][1]:
        color = balls[j][0]
        size = balls[j][1]
        if color in color_sum:
            color_sum[color] += size
        else:
            color_sum[color] = size
        total_sum += size
        j += 1
    
    tmpC = balls[i][0]
    tmpS = balls[i][1]
    tmpI = balls[i][2]

    results[tmpI] = total_sum - color_sum.get(tmpC, 0)

for result in results:
    print(result)

