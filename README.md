# 32st_study

알고리즘 스터디 32주차

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [트럭](https://www.acmicpc.net/problem/13335)

### [민웅](./트럭/민웅.py)

```py
# 13335_트럭_Truck
import sys
from collections import deque
input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))

bridge = deque()

time = 0
total = 0

while True:
    if not bridge and not trucks:
        break
    time += 1
    if bridge:
        out_w, t = bridge[0]
        if time - W == t:
            bridge.popleft()
            total -= out_w
    if trucks:
        tmp = trucks[0]
        if total + tmp <= L:
            bridge.append([trucks.popleft(), time])
            total += tmp

print(time)
```

### [상미](./트럭/상미.py)

```py

```

### [성구](./트럭/성구.py)

```py
```

### [영준](./트럭/영준.py)

```py
```

<br/>

## [컬러볼](https://www.acmicpc.net/problem/10800)

### [민웅](./컬러볼/민웅.py)

```py
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

```

### [상미](./컬러볼/상미.py)

```py

```

### [성구](./컬러볼/성구.py)

```py

```

### [영준](./컬러볼/영준.py)

```py
```

<br/>

## [미친 아두이노](https://www.acmicpc.net/problem/8972)

### [민웅](./미친%20아두이노/민웅.py)

```py
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
```

### [상미](./미친%20아두이노/상미.py)

```py

```

### [성구](./미친%20아두이노/성구.py)

```py
```

### [영준](./미친%20아두이노/영준.py)

```py

```

<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

<br/>

## [나무 높이](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYFofW8qpXYDFAR4&categoryId=AYFofW8qpXYDFAR4&categoryType=CODE)

### [민웅](./나무%20높이/민웅.py)

```py
# SW_나무높이
# 30
# 3 2 5 5 5 4 4 5 2 4 3 4 3 5 5 2 5 4 2 5 2 1 5 4 4 3 2 4 2 4
# 2 3 0 0 0 1 1 0 3 1 2 1 2 0 0 3 0 1 3 0 3 4 0 1 1 2 3 1 3 1
# 2 0 0 0 0 1 1 0 0 1 2 1 2 0 0 0 0 1 0 0 0 4 0 1 1 2 0 1 0 1
# 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2
# 14
# 2 2 2 3 2 2 3 4

# 짝수날이 많은예제
# 8
# 2 2 2 3 2 3 2 4
# 2 2 2 1 2 1 2 0
# 1 1 2 2 2 2 2
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    goal = max(trees)

    for i in range(N):
        trees[i] = goal - trees[i]

    ans = 0
    # 홀수만큼 높이가 부족한날
    one = 0
    # 홀수만큼 높이가 부족한날에서 1씩 빼고 남은 전부
    remain = 0
    for i in range(N):
        tmp = trees[i]
        if tmp % 2:
            trees[i] -= 1
            # 높이가 홀수만큼 남는 날
            one += 1
        remain += trees[i]

    # (홀수날짜에서 1씩 빼고, 다 더한값) // 2 = 짝수날 기를수 있는날
    remain = remain//2

    # 3가지 경우로 나눠서
    if one > remain:
        # 홀수날짜가 많으면 짝수날을 전부 홀수날 사이사이에 끼워넣음 = remain*2
        # +1 다 넣고 바로 다음 첫날
        # 그 뒤로 남은 홀수날짜는 2일마다 한번씩 줄수있음 = 2*(one-1 + remain)
        ans = remain*2 + 1 + 2*(one-remain-1)
    elif one == remain:
        ans = remain*2
    else:
        # 짝수날짜가 많은경우 홀수날을 짝수날에 끼워넣음 = one*2
        # 남은 짝수날을 2가지 경우로 나눠서 채워넣음
        # 1. 짝수날에 물을줌
        # 2. 홀수날을 2번씩 사용해서 물을줌
        ans = one*2 + 2*(2*(remain-one)//3) + (2*(remain-one)%3)

    print(f'#{tc} {ans}')

```

### [상미](./나무%20높이/상미.py)

```py

```

### [성구](./나무%20높이/성구.py)

```py
```

### [영준](./나무%20높이/영준.py)

```py

```

 

</details>

<br/><br/>

