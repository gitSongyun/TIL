import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 배열의 크기, P: 폭탄 위력
    N, P = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 십자탐색
    # 반복은 P만틈 해야 할 것 같고, 한 번 반복할 때 마다 양 옆으로 다 확인 할 수 있도로 해보자

    # Plus, Minus
    dp = 1
    dm = -1

    cross_sum = []

    # 모든 좌표를 다 확인해 봐야 함
    for i in range(N):
        for j in range(N):
            sum_1 = arr[i][j]
            # 십자 방향 탐색
            for k in range(P):

                # 상, 하, 좌, 우
                new_u = i - k - 1
                new_d = i + k + 1
                new_l = j - k - 1
                new_r = j + k + 1

                if 0 <= new_u < N:
                    sum_1 += arr[new_u][j]

                if 0 <= new_d < N:
                    sum_1 += arr[new_d][j]

                if 0 <= new_l < N:
                    sum_1 += arr[i][new_l]

                if 0 <= new_r < N:
                    sum_1 += arr[i][new_r]

            cross_sum.append(sum_1)


    # 대각선 탐색
    diag_sum = []
    for i in range(N):
        for j in range(N):
            sum_2 = arr[i][j]

            for k in range(P):

                # 왼쪽 위
                new_a = i - 1 - k
                new_b = j - 1 - k
                # 오른쪽 위
                new_c = i - 1 - k
                new_d = j + 1 + k
                # 오른쪽 아래
                new_e = i + 1 + k
                new_f = j + 1 + k
                # 왼쪽 아래
                new_g = i + 1 + k
                new_h = j - 1 - k

                if 0 <= new_a < N and 0 <= new_b < N:
                    sum_2 += arr[new_a][new_b]
                if 0 <= new_c < N and 0 <= new_d < N:
                    sum_2 += arr[new_c][new_d]
                if 0 <= new_e < N and 0 <= new_f < N:
                    sum_2 += arr[new_e][new_f]
                if 0 <= new_g < N and 0 <= new_h < N:
                    sum_2 += arr[new_g][new_h]

            diag_sum.append(sum_2)
    result = cross_sum + diag_sum


    for i in range(N*N*2-1):
        if result[i] > result[i+1]:
            result[i], result[i+1] = result[i+1], result[i]

    print(f"#{tc} {result[-1]}")



