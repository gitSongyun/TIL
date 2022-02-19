# 2001_파리퇴치
# 2022-02-19

import sys
sys.stdin = open('input.txt')

T = int(input())

# 가장 많은 파리를 죽이는 경우를 계산할 함수
def calc_1(list, N, M):
    max_1 = 0

    # NxN 행렬에 MxM 칸 사각형을 그릴 수 있는 횟수만큼 반복해야 한다.
    for x in range(N-M+1):
        for y in range(N-M+1):
            sum_1 = 0
            # MxM 사각형 만들기
            for i in range(M):
                for j in range(M):
                    # 사각형 안의 원소들의 합을 구한다.
                    sum_1 += list[i+x][j+y]
            # 그 합이 max_1 보다 크면 갱신한다.
            if max_1 < sum_1 :
                max_1 = sum_1

    return max_1


for tc in range(1, T+1):
    # N : 배열의 크기, M : 파리채 크기
    N, M = list(map(int, input().split()))
    # print(N,M)
    fly = []
    for _ in range(N):
        fly.append(list(map(int, input().split())))

    result = calc_1(fly,N,M)
    print("#{} {}".format(tc, result))
