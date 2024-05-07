T = int(input())
ans = []
for tc in range(1, T+1):
    N = int(input())
    height = list(map(int , input().split()))
    days = 0
    height.sort(reverse=True)
    odd = even = 0          # odd 반드시 홀수날 물을 줘야하는 횟수, even 짝수날 물주기 횟수. 키크기 2는 1+1로 대체 가능
    for i in range(1, N):
        odd += (height[0] - height[i])%2        # 차이가 홀수, 예를 들어 5면 최소 한번은 홀수날 물을 줘야함.
        even += (height[0] - height[i])//2   # 2만큼 성장시키는 횟수

    if odd>even:            # 1 성장이 2 성장보다 많은 경우, 예) 1 2 3 4 5일에 물주기
        days = odd * 2 - 1
    elif odd==even:         # 예) 1 2 3 4에 물주기
        days = odd * 2
    elif odd<even:
        days += odd*2       # 예) [1 2] 4 6 ... odd는 반드시 지켜야 하므로
        even -= odd         # odd==even으로 만든 만큼 제외
        days += even//3*4   # [1 2] 4 6 8 10... -> 4 6 8(6일)을 3 4 5 6(4일)에 키울 수 있음 8일차 2를 3,5일에 1씩 나눠 기움
        if even%3==2:       # [1 2] 4 6처럼 2가 두개 남으면 3 4 5처럼 3일로 키울 수 있고
            days += 3
        elif even%3==1:     # [1 2] 4처럼 2가 하나 남으면 짝수날 물주는게 유리하다.
            days += 2
    ans.append(days)
for i in range(T):
    print(f'#{i+1} {ans[i]}')
