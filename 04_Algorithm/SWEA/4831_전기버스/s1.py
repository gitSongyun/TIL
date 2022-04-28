# 4831_전기버스
# 2022-02-10

import sys
sys.stdin=open("sample_input.txt")


T = int(input()) # 노선의 수

for i in range (1, T+1):
    K, N, M = map(int, input().split()) # K= 최대이동, N= 목적지 , M= 충전 정류장 갯수
    charge = list(map(int, input().split())) # 충전소 정류장 번호

    # 정류장을 list로 생성
    bustop = [0] * (N + 1)
    for j in range(M):
        # 충전기가 있는 버스정류장 구분
        bustop[charge[j]] += 1
        # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        # [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0]
        # [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]

    charge_count = last_charge = 0 # 충전 횟수, 최근 충전 위치 0으로 선언
    current = K # 우선 현재위치는 버스가 최대로 움직일 수 있는 거리로 선언

    # 현재위치가 목적지 이상이 될 때 까지 반복.
    while current < N:

        # 만약 current를 하나씩 줄이다가 마지막 충전소로 돌아온다면
        if last_charge == current:
            charge_count = 0 # 움직일 수 있는 최대 거리 안에 충천소를 찾지 못하게 되고
            break            # 더 이상 움직이지 못하게 된다.

        # 현재 정류장에 충전소가 있다면
        if bustop[current]:
            last_charge = current  # 최근 충전위치를 현재위치로 만들고
            charge_count += 1      # charge_count에 1을 더한다.
            current += K           # 충전을 했으니 다시 최대로 이동한다.

        # 현재 정류장에 충전소가 없다면 현재 위치를 하나씩 줄여나가서 충전소 위치를 찾는다.
        else:
            current -= 1

    ans = charge_count
    print('#{} {}' .format(i, ans))









