# 1974_스도쿠 검증
# 2022-02-20

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    result = 1
    # 스도쿠 퍼즐 받아오기
    arr = [list(map(int,input().split())) for _ in range(9)]

    # 가로비교
    for i in range(9):
        sum_r = 0
        for j in range(9):
            sum_r += arr[i][j]

        if sum_r != 45:
            result = 0
            break

    # 세로비교
    for j in range(9):
        sum_c = 0
        for i in range(9):
            sum_c += arr[i][j]

        if sum_c != 45:
            result = 0
            break

    # 3X3 비교
    for a in range(0, 9, 3): # 0 3 6
        for b in range(0, 9, 3):
            cnt = 0
            for i in range(3):
                for j in range(3):
                    cnt += arr[i+a][j+b]

            if cnt != 45:
                result = 0
                break

    print("#{} {}".format(tc,result))
