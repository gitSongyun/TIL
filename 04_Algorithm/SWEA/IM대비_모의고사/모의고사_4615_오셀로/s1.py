# 4615_오셀로
# 2022-03-27

import sys
sys.stdin = open('sample_input(1).txt')

T = int(input())

for tc in range(1, T+1):
    # N = 판의 크기, M = 돌을 놓는 횟수
    N, M = list(map(int, input().split()))

    # 판 행렬로 생성
    board = [[0]*(N) for _ in range(N)]

    center = (N - 1) // 2
    # B = 1 W = 2 가운데 2*2로 기본 세팅 만들어주기
    board[center][center] = 2
    board[center][center + 1] = 1
    board[center + 1][center] = 1
    board[center + 1][center + 1] = 2

    for i in range(M):
        # r은 행, c는 열, x는 돌의 색깔
        r, c, x = list(map(int,input().split()))
        r -= 1
        c -= 1

        # 11시 방향부터 시계방향으로,
        for j in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):

            # 범위를 한 칸씩 넓혀가며 탐색
            for k in range(1, N): # ex) k = 1, 2, 3
                nr = r + j[0] * k
                nc = c + j[1] * k
                if 0 <= nr < N and 0 <= nc < N:

                    # 탐색중에 0을 만나거나 바로 다음에 같은 색이 있다면 현재 방향 탐색 종료
                    if board[nr][nc] == 0 or board[r+j[0]][c+j[1]] == x:
                        break

                    # 다른 색을 만나면 그 다음 칸을 한 번더 봐야 한다.
                    elif board[nr][nc] != x:
                        continue

                    # 그러다가 같은 색을 만나면
                    elif board[nr][nc] == x:
                        # 돌을 놓을 수 있고
                        board[r][c] = x
                        for a in range(1, k):
                            # 지나온 칸 수 만큼 되돌아가며 같은 색으로 바꿔 준다.
                            board[nr-j[0]*a][nc-j[1]*a] = x

        # 흑, 백 돌의 갯수
        b_sum = w_sum = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    w_sum += 1
                elif board[i][j] == 2:
                    b_sum += 1

    print('#{} {} {}'.format(tc, w_sum, b_sum))




