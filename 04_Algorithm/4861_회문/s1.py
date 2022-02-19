# 4861_회문
# 2022-02-17

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 행렬 크기, M: 회문의 길이
    N, M = map(int,input().split())

    # 입력받은 리스트
    list_a = []
    for k in range(N):
        list_a.append(list(input()))

    # 세로 판별을 위한 전치행렬
    list_b = [[0] * N for _ in range(N)]

    cnt_r = 0 # row에서 회문을 찾을 때 쓸 cnt
    cnt_c = 0 # col에서 회문을 찾을 때 쓸 cnt

    # 세로 판별은 전치행렬로 만들어서 행과 열을 동시에 비교한다.
    for a in range(N):
        for b in range(N):
            list_b[a][b] = list_a[b][a]


    for i in range(N): # 행과 열이 N개니까 N번 반복
        for k in range(N - M + 1): # 슬라이싱 횟수

            # 행, 열 슬라이싱
            row_list = list_a[i][k: M+k] 
            col_list = list_b[i][k: M+k]

            # 잘라낸 리스트의 양쪽 끝을 비교 하겠다. 비교는 회문길이의 절반만 하면 된다.
            for j in range(M//2):
                
                # 양끝이 같다면 +1을 하고
                if row_list[j] == row_list[-j-1]:
                    cnt_r += 1
                    # cnt_r 이 회문 길이의 절반과 같아진다면 회문이 된다.
                    if cnt_r == M//2:
                        ans_list = row_list

                else:
                    cnt_r = 0

                if col_list[j] == col_list[-j-1]:
                    cnt_c += 1
                    if cnt_c == M//2:
                        ans_list = col_list

                else:
                    cnt_c = 0


    result = "".join(ans_list)
    print("#{} {}" .format(tc, result))

# 잘못한 점
# 34,35번 줄에서 슬라이싱 범위를 잘 못 지정하였다. [k: M+k]를 해야 하는데 [k: M]로 했다.