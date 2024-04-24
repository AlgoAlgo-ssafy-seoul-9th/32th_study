import sys
input = sys.stdin.readline
from collections import deque

n, w, L = map(int, input().split())
trains = list(map(int, input().split()))
bridge = deque()                # 현재 다리 위
tmp = trains[0]                     # 현재 다리 위 무게
i = 1                       # 기차 인덱스
time = 1
bridge.append([trains[0], w])
while i < n:
    for b in range(len(bridge)):
            bridge[b][1] -= 1
    if bridge[0][1] == 0:
        tmp -= bridge[0][0]
        bridge.popleft()
    if tmp + trains[i] <= L:             # 다음 기차 올라갈 수 있으면
        tmp += trains[i]            # 이번 기차 무게 올라가고
        bridge.append([trains[i], w])   # [무게, 남은 길이] 추가
        i += 1
    
    time += 1
print(time+w)


