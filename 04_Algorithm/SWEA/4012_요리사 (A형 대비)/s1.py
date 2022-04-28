from itertools import combinations, permutations
import sys
sys.stdin = open('sample_input.txt')

# (1,2) (2,1) 이런 인덱스 끼리의 값을 더해야 한다.
# 이미 선택한 식재료라면 제외하고 다른 식재료를 선택해야 한다.

T = int(input())

for tc in range(1, T+1):
    # 식재료 갯수
    N = int(input())

    # 시너지 표
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 식재료 갯수에 따른 인덱스 조합
    N_idx = [i for i in range(N)]

    # 한 요리에는 N//2 개의 식재료가 들어간다.
    com_a = list(combinations(N_idx, N//2))

    # com_a를 거꾸로 출력하여 식재료가 겹치지 않게 '조합' 을 맞춘다.
    com_b = []
    for j in range(len(com_a)):
        com_b.append(com_a[len(com_a)-j-1])


    # 시너지 합을 넣을 결과 리스트
    result = []

    # len(com_a)//2 이후로는 조합이 겹치므로.
    for k in range(len(com_a)//2):

        # 각 식재료를 사용하였을 때 시너지 결과를 담을 변수
        food_a = food_b = 0

        # a 음식의 시너지 값
        for i in combinations(com_a[k], 2):
            # print(i)
            r1 = i[0]
            c1 = i[1]
            food_a += arr[r1][c1] + arr[c1][r1]

        for i in combinations(com_b[k], 2):
            r2 = i[0]
            c2 = i[1]
            food_b += arr[r2][c2] + arr[c2][r2]

        sum = abs(food_a - food_b)

        result.append(sum)
    print("#{} {}" .format(tc, min(result)))
