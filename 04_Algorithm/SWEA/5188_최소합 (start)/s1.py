# 5188_최소합
# 2022-03-29
import sys
sys.stdin = open('sample_input.txt')

def DFS(s, ssum):
    global ans

    # 가지치기
    # 탐색 도중 ssum 이 ans 보다 커지면 리턴
    if ssum >= ans:
        return

    # 도착점에 도착했을 때
    if s[0] == N-1 and s[1] == N-1:
        # 누적합과 저장된 최소값을 비교하여 ans를 갱신한다.
        if ssum <= ans:
            ans = ssum


    # 왼쪽에서 아래 방향으로 탐색
    for i in ((1, 0), (0, 1)):  # 하 우
        nr = s[0] + i[0]
        nc = s[1] + i[1]

        if 0 <= nr < N and 0 <= nc < N:
            DFS([nr, nc], ssum+arr[nr][nc])

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 배열 크기

    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 999

    DFS([0, 0], arr[0][0])
    print("#{} {}".format(tc, ans))

# import sys
# sys.stdin = open('sample_input.txt')
#
# def DFS(s, path):
#     global ans, ssum
#
#     if ssum >= ans:
#
#         return
#
#     if s[0] == N-1 and s[1] == N-1:
#         # print(path, ssum)
#         if ssum <= ans:
#             ans = ssum
#             return ans
#
#     for i in ((1, 0), (0, 1)):  # 하 우
#         nr = s[0] + i[0]
#         nc = s[1] + i[1]
#
#         if 0 <= nr < N and 0 <= nc < N:
#             ssum += arr[nr][nc]
#             DFS([nr, nc], path + str(arr[nr][nc]))
#             ssum -= arr[nr][nc]
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())  # 배열 크기
#
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 999
#     path = ''
#     ssum = arr[0][0]
#     DFS([0, 0], path)
#     print('#{} {}'.format(tc, ans))
