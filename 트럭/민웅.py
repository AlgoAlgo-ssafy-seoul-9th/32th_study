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