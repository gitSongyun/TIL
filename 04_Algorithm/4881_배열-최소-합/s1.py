import sys
sys.stdin = open('sample_input.txt')


def DFS(r, sum_1, visited):
    global ans

    if sum_1 > ans:
        return

    # 종료조건
    if r >= N:
        if sum_1 < ans:
            ans = sum_1
        return


    # 열의 갯수만큼 반복 해야 한다.
    for i in range(N):
        # i번째 열이 방문하지 않았고
        if not visited[i]:
            visited[i] = True
            DFS(r+1, sum_1+arr[r][i], visited)
            visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 배열의 크기

    arr = [list(map(int,input().split())) for _ in range(N)]

    # 경우의 수 합을 담을 변수

    ans = 99
    # 열(column)의 방문 여부를 저장
    visited = [False] * N
    DFS(0, 0, visited)
    print("#{} {}".format(tc, ans))