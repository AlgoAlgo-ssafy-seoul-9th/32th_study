# 8972_미친아두이노_crazy arduino
import sys
input = sys.stdin.readline
dxy = [(0, 0), (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

R, C = map(int, input().split())

field = [list(input().strip()) for _ in range(R)]
player = []
ardu = set()
for i in range(R):
    for j in range(C):
        if field[i][j] == 'I':
            player = [i, j]
        elif field[i][j] == 'R':
            ardu.add((i, j))

moves = list(map(int, input().strip()))
cnt = 0
is_end = False
for m in moves:
    cnt += 1
    nx = player[0] + dxy[m][0]
    ny = player[1] + dxy[m][1]
    player = [nx, ny]

    a_tmp = set()
    # 추가
    a_remove = set()
    for a in ardu:
        tmp_x = nx - a[0]
        if tmp_x < 0:
            ax = -1
        elif tmp_x > 0:
            ax = 1
        else:
            ax = 0
        tmp_y = ny - a[1]
        if tmp_y < 0:
            ay = -1
        elif tmp_y > 0:
            ay = 1
        else:
            ay = 0
        ax = a[0] + ax
        ay = a[1] + ay
        if ax == nx and ay == ny:
            is_end = True
            break
        if (ax, ay) in a_tmp:
            a_remove.add((ax, ay))
        else:
            a_tmp.add((ax, ay))
    # 추가
    for x, y in a_remove:
        a_tmp.remove((x, y))
    if is_end:
        break

    ardu = a_tmp

if is_end:
    print(f"kraj {cnt}")
else:
    ans = [['.']*C for _ in range(R)]
    for a in ardu:
        ans[a[0]][a[1]] = "R"

    ans[player[0]][player[1]] = "I"

    for line in ans:
        print(*line, sep="")