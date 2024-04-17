# 32st_study

알고리즘 스터디 32주차

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [문제1](문제주소)

### [민웅](./문제1/민웅.py)

```py

```

### [상미](./문제1/상미.py)

```py

```

### [성구](./문제1/성구.py)

```py
```

### [영준](./문제1/영준.py)

```py
```

<br/>

## [문제2](문제주소)

### [민웅](./문제2/민웅.py)

```py

```

### [성구](./문제2/성구.py)

```py

```

### [영준](./문제2/영준.py)

```py
```

<br/>

## [문제3](문제주소)

### [민웅](./문제3/민웅.py)

```py
```

### [상미](./문제3/상미.py)

```py

```

### [성구](./문제3/성구.py)

```py
```

### [영준](./문제3/영준.py)

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
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    goal = max(trees)

    for i in range(N):
        trees[i] = goal - trees[i]

    ans = 0
    one = 0
    remain = 0
    for i in range(N):
        tmp = trees[i]
        if tmp % 2:
            trees[i] -= 1
            # 높이가 홀수만큼 남는 날
            one += 1
        remain += trees[i]

    # 홀수날짜에서 1씩 빼고, 나머지를 다 더한값 //2 = 짝수날 기를수 있는날
    remain = remain//2

    # 3가지 경우로 나눠서
    if one > remain:
        ans = remain*2 + 1 + 2*(one-remain-1)
    elif one == remain:
        ans = remain*2
    else:
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

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
