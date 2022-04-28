import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # print("{}번 케이스".format(tc))
    K, N, M = list(map(int, input().split())) # K: 이동가능, K: 이동가능, M: 충전소 갯수
    charge = list(map(int, input().split()))
    # bus_stop = [4, 7, 9, 14, 17]


    current = 0
    cnt = 0
    last_charge = 0
    # 최대 이동 거리만큼 움직인 후 그곳이 충전소가 아니라면 돌아온다.
    # 한 칸씩 돌아오면서 충전소가 있는지 확인한다.
    # 있다면 충전하고, 마지막 충전위치 갱신하고 다시 이동 한다.

    while current < N:
        # print(current)
        # 최대 이동 거리 이동
        current += K

        if current >= N:
            break

        a = 0
        # 한 칸 씩 뒤로 돌리는 반복문
        for i in range(K+1):

            # 만약 현재 위치가 충전소라면
            if current in charge:
                # 최근 충전 위치를 현재 위치로 바꾸고 break 한다.
                last_charge = current
                cnt += 1
                break

            # 아니라면 한 칸 앞으로 땡긴다.
            else:
                current -= 1
                # 뒤로 한칸 씩 돌아오다가 마지막 충전 위치로 돌아온다면 반복문 종료
                if current == last_charge:
                    cnt = 0
                    a = 1
                    break

        # 반복문 완전히 종료
        if a == 1:
            break

    print("#{} {}".format(tc, cnt))