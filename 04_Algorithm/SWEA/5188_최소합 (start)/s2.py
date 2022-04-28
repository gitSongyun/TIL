import sys
sys.stdin = open('sample_input.txt')


def DFS(s, ssum):
    global ans

    # 종료조건
    if s[0] == N-1 and s[1] == N-1:
        if ssum <= ans:
            ans = ssum


    r = s[0]
    c = s[1]
    for k in ((1, 0), (0, 1)):
        nr = r + k[0]
        nc = c + k[1]

        if 0 <= nr < N and 0 <= nc < N:
            DFS([nr, nc], ssum+arr[nr][nc])

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    ans = 9999


    DFS([0,0], arr[0][0])
    print(ans)