# 10800 컬러볼
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    N = int(input())
    colorballs = []
    for i in range(N):
        colorballs.append((i, *map(int, input().split())))
    
    colors = defaultdict(int)
    prefix, same = 0, 0
    same_color = defaultdict(int)
    sequence = [0] * N
    sort_colorballs =  sorted(colorballs, key=lambda x:(x[2], x[1]))
    for i in range(N-1):
        idx, c, ball = sort_colorballs[i]
        _, _, post_ball = sort_colorballs[i+1]
        if ball == post_ball:
            sequence[idx] = prefix - colors[c]
            same_color[c] += 1
            same = ball
        else:
            sequence[idx] = prefix - colors[c]
            if same_color:
                for prev_c, cnt in same_color.items():
                    colors[prev_c] += same * cnt
                    prefix += same * cnt
                same_color.clear()
            prefix += ball
            colors[c] += ball

    idx, c, ball = sort_colorballs[-1]
    sequence[idx] = prefix - colors[c]


    print(*sequence, sep="\n")
    return 


if __name__ == "__main__":
    main()