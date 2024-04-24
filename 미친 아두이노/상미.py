import sys
input = sys.stdin.readline

def jongsu(di):
    global cnt
    if di == 1:
        jong[0] += 1
        jong[1] -= 1
    elif di == 2:
        jong[0] += 1
    elif di == 3:
        jong[0] += 1
        jong[1] += 1
    elif di == 4:
        jong[1] -= 1
    elif di == 6:
        jong[1] += 1
    elif di == 7:
        jong[0] -= 1
        jong[1] -= 1
    elif di == 8:
        jong[0] -= 1
    elif di == 9:
        jong[0] -= 1
        jong[1] += 1
    cnt += 1
    
def Arduino(tx, ty, crazy):
    for i in range(len(crazy)):
        if tx < crazy[i][0] and ty < crazy[i][1]:
            crazy[i][0] -= 1
            crazy[i][1] -= 1
        elif tx == crazy[i][0] and ty < crazy[i][1]:
            crazy[i][1] -= 1
        elif tx > crazy[i][0] and ty < crazy[i][1]:
            crazy[i][0] += 1
            crazy[i][1] -= 1
        elif tx > crazy[i][0] and ty == crazy[i][1]:
            crazy[i][0] += 1
        elif tx > crazy[i][0] and ty > crazy[i][1]:
            crazy[i][0] += 1
            crazy[i][1] += 1
        elif tx == crazy[i][0] and ty > crazy[i][1]:
            crazy[i][1] += 1
        elif tx < crazy[i][0] and ty > crazy[i][1]:
            crazy[i][0] -= 1
            crazy[i][1] += 1
        elif tx < crazy[i][0] and ty == crazy[i][1]:
            crazy[i][0] -= 1

def sameArd(crazy):
    ADict = {}
    for [cx, cy] in crazy:
        ADict[(cx, cy)] = ADict.get((cx, cy), 0) + 1
    for key, value in ADict.items():
        if value > 1:
            for _ in range(value):
                crazy.remove([key[0], key[1]])

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
move = list(input().strip())
jong = [0, 0]
cnt = 0
crazy = []
Gameover = False
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'I':
            jong = [i, j]
        elif arr[i][j] == 'R':
            crazy.append([i, j])
for m in move:
    jongsu(int(m))              # 종수 이동
    Arduino(jong[0], jong[1], crazy)        # 아두이노들 이동

    for cx, cy in crazy:                    # 아두이노와 종수 만나면 종료
        if cx == jong[0] and cy == jong[1]:
            print("kraj", cnt)
            Gameover = True
            break
    if Gameover:
        break
    sameArd(crazy)              # 같은 위치의 아두이노들 폭발
   
if not Gameover:
    ans = [['.']* C for _ in range(R)]
    for cx, cy in crazy:
        ans[cx][cy] = 'R'
    ans[jong[0]][jong[1]] = 'I'
    for r in range(R):
        print(''.join(ans[r]))
