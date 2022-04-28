# 5688_세제곱근을-찾아라
# 2022-03-18
import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    # N을 1/3 제곱을 한 후에 반올림 하고, 정수로 바꾼다.
    result = (int(round(N ** (1 / 3))))

    # 그 결과에 3제곱을 했을 때 N 이 아니라면 -1 출력
    if result ** 3 != N:
        print("#{} {}".format(tc, -1))

    # 맞다면 result를 출력
    else:
        print("#{} {}".format(tc, result))