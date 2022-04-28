import sys

sys.stdin = open('input.txt')

def FIND(r, rate):
    global ans
    print(ans)

    # N번째 사람 까지 봤다면
    if r == N:
        # rate 가 최대가 되면 ans 를 갱신한다.
        if rate > ans:
            ans = rate
            return

    if rate < ans:
        return

    # i는 일(column), r은 사람(row) 의미
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            FIND(r+1, rate*(work[r][i])/100)
            visited[i] = False

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 사람 수
    work = [list(map(int, input().split())) for _ in range(N)]
    # [13, 0, 50]
    # [12, 70, 90]
    # [25, 60, 100]
    visited = [False] * N
    ans = 0
    FIND(0, 1)
    ans *= 100
    print(f'#{tc} {"%.6f" %ans}')