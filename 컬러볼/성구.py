# 10800 컬러볼
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    N = int(input())
    colorball = []
    colormax = 0
    sequence = [0] * N
    for i in range(N):
        c, b = map(int, input().split())
        colorball.append([i, c, b])
        colormax = max(colormax, c)
    
    colorball.sort(key=lambda x:(x[2], x[1]))
    
    color = [0] * (colormax+1)
    balls = [0] * N
    
    color[colorball[0][1]] = colorball[0][2]
    balls[0] = colorball[0][2]
    pin = 0
    same = 0
    for i in range(1, N):
        if colorball[i][2] != colorball[i-1][2]:
            break
        color[colorball[i][1]] = colorball[i][2]
        same += colorball[i][2]
        balls[i] = colorball[i][2]
        pin = i
    
    for i in range(pin+1, N):
        idx, c, b = colorball[i]
        color[c] += b 
        if b == colorball[i-1][2]:
            balls[i] = balls[i-1]
            same += b
        else:
            balls[i] = balls[i-1] + b + same
            same = 0
        if colorball[i-1][1] == c:
            sequence[idx] = balls[i]-color[c] + same
        else:
            sequence[idx] = balls[i]-color[c] 

    print(*sequence, sep="\n")

    return 


if __name__ == "__main__":
    main()