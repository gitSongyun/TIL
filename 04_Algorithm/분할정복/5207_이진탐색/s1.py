# 5207_이진탐색
# 2022-03-31

import sys
sys.stdin = open('sample_input.txt')

def EXP(m, l, r, f):

    global cnt

    # 종료조건
    if A[m] == B[f]:
        cnt += 1
        return

    # 찾는 값이 m보다 크다면 오른쪽 탐색
    elif A[m] < B[f]:
        l = m + 1
        m = (r+l) // 2

        # 오른쪽을 탐색했다면 다음은 반대쪽을 탐색해야 한다.
        # 새로운 m 기준으로 찾는 값이 왼쪽에 있을 때만 찾겠다.
        if A[m] >= B[f]:
            EXP(m, l, r, f)


    # 찾는 값이 m보다 작다면 왼쪽 탐색
    elif A[m] > B[f]:

        r = m - 1
        m = (r+l) // 2
        # 왼쪽 탐색 후 새로운 A[m]보다 B[f] 값이 커야 오른쪽 탐색이 가능.
        if A[m] <= B[f]:
            EXP(m, l, r, f)


T = int(input())

for tc in range(1, T+1):
    # N : A의 길이, M : B의 길이
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()

    l = 0           # left
    r = N-1         # right
    m = (r+l) // 2  # middle
    cnt = 0

    for f in range(M):
        EXP(m, l, r, f) # f = 찾고자 하는 값
    print("#{} {}".format(tc, cnt))