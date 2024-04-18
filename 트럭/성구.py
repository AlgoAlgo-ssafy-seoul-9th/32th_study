# 13335 트럭
import sys
input = sys.stdin.readline


def main():
    n, w, l = map(int, input().split())
    trucks = tuple(map(int, input().split()))

    bridge = [-1] * w
    
    weight = 0
    t = 0
    
    truck_idx = 0
    while truck_idx < n :
        # 다리 위에 트럭이 있을 때에만 트럭 무빙(처음 1번은 움직일 필요없음)
        if weight:
            # 만약 다리 끝까지 온 트럭이 있으면 무게 빼줌
            if bridge[0] >= 0:
                weight -= trucks[bridge[0]]
                bridge[0] = -1
            # 트럭움직임
            for i in range(w-1):
                bridge[i] = bridge[i+1]
            # 마지막 비워주기
            bridge[-1] = -1
        
        # 무게 하중을 다리가 버틸 수 있으면 트럭 올리기
        if weight + trucks[truck_idx] <= l:
            bridge[-1] = truck_idx
            # 무게 추가
            weight += trucks[truck_idx]
            # 다음 인덱스 탐색
            truck_idx += 1
    
        t += 1  # 시간 증가

        # 디버깅
        # print(f'트럭 인덱스: {truck_idx}, 시간: {t}')
        # print(f'다리 위 트럭 무게 : {weight}')
        # print(f'다리 현황 : {bridge}')

    # 다리 위에 남아 있는 트럭 처리
    # 마지막 인덱스만 알면 인덱스 + 1만큼의 시간이 추가로 소요된다.
    additional = -1
    for i in range(w-1, -1, -1):
        if bridge[i] >= 0:
            additional = i
            break
    
    print(t + additional+1)

    return


if __name__ == "__main__":
    main()