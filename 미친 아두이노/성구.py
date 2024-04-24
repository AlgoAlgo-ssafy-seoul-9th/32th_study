# 8972 미친 아두이노
import sys
input = sys.stdin.readline


def main():
    R, C = map(int, input().split())
    field = [list(input().strip()) for _ in range(R)]
    order = tuple(map(int, (input().strip())))
    direction = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0,1) ,(-1,-1),(-1,0),(-1,1)]
    I = []
    robots = {}
    
    def distance(y1, x1, y2, x2):
        return abs(y1-y2) + abs(x1-x2)

    def move_robots(target_i, target_j):
        tmp = [["."] * C for _ in range(R)]
        for idx in robots.keys():
            i, j = robots[idx]
            minv = 100001
            cand = (i,j)
            for di, dj in direction:
                if di== 0 and dj == 0:
                    continue
                ni, nj = di+i, dj+j
                if not (0 <= ni < R) or not(0<=nj<C):
                    continue
                d = distance(target_i, target_j, ni, nj)
                if minv > d:
                    minv = d
                    cand = (ni,nj)
            
            if cand[0] == target_i and cand[1] == target_j:
                return 1
            
            
            field[i][j] = "."
            if tmp[cand[0]][cand[1]] == "R":
                boom.add(cand)
                boom.add((i,j))
            else:
                tmp[cand[0]][cand[1]] = "R" 
                # field[cand[0]][cand[1]] = "R" 
                robots[idx] = (cand[0], cand[1])
        return 0
    
    def boom_robot():
        robokey = list(robots.keys())
        for key in robokey:
            if robots[key] in boom:
                field[robots[key][0]][robots[key][1]] = "."
                robots.pop(key)
        boom.clear()
        for key in robots.keys():
            field[robots[key][0]][robots[key][1]] = "R"
        return 
    
    def find():
        cnt = 0
        for i in range(R):
            for j in range(C):
                if field[i][j] == "I":
                    I = [i,j]
                elif field[i][j] == "R":
                    robots[cnt] = (i,j)
                    cnt += 1
        return I

    I = find()
    ans = -1
    boom = set()
    for cnt in range(len(order)):
        o = order[cnt] - 1
        ni,nj = direction[o][0]+I[0], direction[o][1]+I[1]
        if field[ni][nj] == "R":
            ans = cnt+1
            break
        field[I[0]][I[1]] = "."
        field[ni][nj] = "I"
        I= [ni,nj]
        if move_robots(ni, nj):
            ans = cnt+1
            break
        boom_robot()

    if ans == -1:
        [print(''.join(field[y])) for y in range(R)]
    else:
        print(f'kraj {ans}')
    return


if __name__ == "__main__":
    main()