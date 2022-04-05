# 5208_전기버스2
# 2022-04-02
import sys
sys.stdin = open('sample_input.txt')

def DFS(s, cnt): # s = 2
    global ans
    print(s)
    # 종료조건, 현재 위치가 종점에 도착했을 때
    if s >= bus[0]-1:
        if cnt <= ans:
            ans = cnt
        return

    if cnt >= ans:
        return

    # 현재 위치에서 배터리를 교환한다.
    bat = bus[s]

    # 현재 배터리 만큼 갈 수 있는 곳의 경우의 수가 생긴다.
    for i in range(s+bat, s, -1): # 1, 2, 3
        DFS(i, cnt+1)

T = int(input())

for tc in range(1, T+1):

    bus = list(map(int, input().split()))
    bus += [0] * bus[0] # 인덱스 에러 방지
    cnt = -1

    ans = 9999999999
    DFS(1, cnt)

    print("#{} {}".format(tc, ans))

import sys

sys.stdin = open('sample_input.txt')


def dfs(cnt, pos):
    print(pos)
    global min_value
    if min_value <= cnt:
        return
    if N - 1 <= pos:
        if cnt <= min_value:
            min_value = cnt
        return

    for i in range(A[pos]):
        dfs(cnt + 1, i + 1 + pos)


T = int(input())

for tc in range(1, T + 1):
    A = list(map(int, input().split()))

    N = A[0]
    A = A[1:]
    min_value = 10000

    dfs(-1, 0)
    print('#{} {}'.format(tc, min_value))