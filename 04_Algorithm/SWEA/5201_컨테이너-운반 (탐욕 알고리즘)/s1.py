# 5201_컨테이너-운반 풀이
# 2022-03-29
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N : 컨테이너 갯수, M : 트럭 갯수

    # 컨테이너의 무게와 가장 비슷한 트럭을 찾기 위해
    # 컨테이너 무게는 내림차순, 트럭은 오름차순으로 정렬한다.
    cont = list(map(int,input().split()))
    cont = sorted(cont, reverse=True)
    tr = sorted(list(map(int,input().split())))

    ssum = 0

    # 컨테이너의 갯수만큼 반복
    for i in range(N):
        # i번 컨테이너를 실을 수 있는 가장 작은 트럭
        for j in range(len(tr)):
            # 최적의 트럭을 찾았다면
            if cont[i] <= tr[j]:
                # 컨테이너의 무게를 더해주고
                ssum += cont[i]
                # 그 트럭은 제외 한다.
                tr.pop(j)
                # 다음 컨테이너 탐색
                break

        # 트럭이 다 제외 됐다면 종료한다.
        if not tr:
            break
    print("#{} {}".format(tc, ssum))
