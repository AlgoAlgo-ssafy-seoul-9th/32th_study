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

