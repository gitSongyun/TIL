# 5356_의석이의 세로로 말해요
# 2022-02-20

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 최대 열의 갯수를 찾아낼 함수
def col_num(list):

    max_1 = 0
    for i in range(5):
        if max_1 < len(list[i]):
            max_1 = len(list[i])

    return max_1


for tc in range(1, T+1):

    arr = []
    for _ in range(5):
        arr.append(list(input()))

    # 최대 열의 갯수를 알아낸다.
    col_max = col_num(arr)

    # 정답을 담을 새로운 str
    new_str = ''

    # 최대 열의 갯수만큼 반복을 한다.
    for j in range(col_max):
        for i in range(5):
            # 열 인덱스가 행의 길이를 넘어가면 문자가 존재하지 않는다.
            if len(arr[i]) > j:
                new_str += arr[i][j]

    print("#{} {}".format(tc, new_str))
