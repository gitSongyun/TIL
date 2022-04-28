from itertools import combinations, permutations
import sys
sys.stdin = open('sample_input.txt')

# (1,2) (2,1) 이런 인덱스 끼리의 값을 더해야 한다.
# 이미 선택한 식재료라면 제외하고 다른 식재료를 선택해야 한다.
#

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 식재료 갯수에 따른 인덱스 조합
N_idx = [i for i in range(N)]
com_a = list(combinations(N_idx, N//2))
com_b = []
for j in range(len(com_a)):
    com_b.append(com_a[len(com_a)-j-1])
print(com_a)
# print(com_b)

# com_a = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
# com_b = [(2, 3), (1, 3), (1, 2), (0, 3), (0, 2), (0, 1)]

result = []
# print(com_a)
for k in range(len(com_a)//2):
    food_a = food_b = 0

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
print(min(result))


