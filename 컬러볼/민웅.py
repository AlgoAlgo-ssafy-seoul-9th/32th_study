# 10800_컬러볼_colorball
import sys
# import heapq
input = sys.stdin.readline

N = int(input())

balls = []
ans = [0]*(N+1)
colors = {}
prefix = [0]
for i in range(N):
    c, s = map(int, input().split())
    balls.append([s, c, i+1])

balls.sort()
for i in range(N):
    s, c, idx = balls[i]
    if i < N-1 and balls[i][0] == balls[i+1][0]:
        continue

    sum_size = 0
    for j in range(i, -1, -1):
        if balls[j][0] != s:
            break
        sum_size += s
        if balls[j][1] in colors.keys():
            ans[balls[j][2]] = prefix[-1] - colors[balls[j][1]]
        else:
            colors[balls[j][1]] = 0
            ans[balls[j][2]] = prefix[-1]

    for k in range(i, -1, -1):
        if balls[k][0] != s:
            break
        colors[balls[k][1]] += s

    prefix.append(prefix[-1] + sum_size)


for i in range(1, N+1):
    print(ans[i])
