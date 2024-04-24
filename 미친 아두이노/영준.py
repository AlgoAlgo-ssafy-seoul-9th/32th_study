# 10% 시간초과과
di = [0, 1, 1, 1, 0, 0, 0,-1,-1,-1]
dj = [0,-1, 0, 1,-1, 0, 1,-1, 0, 1]

R, C = map(int, input().split())
bd = [list(input()) for _ in range(R)]
mov = input()
js = [0]*3
arduino = []
for i in range(R):
    for j in range(C):
        if bd[i][j] == 'I':
            js[0], js[1] = i, j
        if bd[i][j] == 'R':
            arduino.append([i,j])
check = [0]*len(arduino)    # 아두이노 폭파

for x in mov:
    x = int(x)
    js[0], js[1] = js[0]+di[x], js[1]+dj[x]

    js[2] += 1      # 이동 횟수
    for p in range(len(arduino)):
        if check[p]==0 and arduino[p]==js[:2]:
            js[0] = -1
            break
    if js[0]==-1:
        break
    visited = [[-1]*C for _ in range(R)]
    for p in range(len(arduino)):
        if check[p]==0:
            min_i = min_j = 0
            min_v = 1000000
            for k in range(1, 10):
                if k!=5:
                    ni, nj = arduino[p][0]+di[k], arduino[p][1]+dj[k]
                    if 0<=ni<R and 0<=nj<C:
                        tmp = abs(js[0]-ni)+abs(js[1]-nj)   # 종수와 거리
                        if min_v > tmp:                     # 최소거리 위치 찾기
                            min_i, min_j = ni, nj
                            min_v = tmp
            arduino[p][0], arduino[p][1] = min_i, min_j
            if arduino[p] == js[:2]:  # 종료
                js[0] = -1
                break   #for p
            if visited[min_i][min_j]!=-1:
                check[visited[min_i][min_j]] = 1
                check[p] = 1
            else:
                visited[min_i][min_j] = p

    else:
        continue
    break

if js[0]==-1:   # 중간 종료
    print(f'kraj {js[2]}')
else:
    ans = [['.']*C for _ in range(R)]
    ans[js[0]][js[1]] = 'I'
    for p in range(len(arduino)):
        if check[p]==0:
            ans[arduino[p][0]][arduino[p][1]] = 'R'
    for x in ans:
        print(''.join(x))
