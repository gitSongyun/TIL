import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # 테스트 케이스 갯수

for tc in range(1, T+1):

    N = int(input()) # 방의 크기
    room = [list(map(int, input().split())) for _ in range(N)]
    man = []
    for i in range(N):
        for j in range(N):
            if room[i][j] == 2:
                man += [i, j]

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni = man[0] + di
        nj = man[1] + dj

        while 0 <= ni < N and 0 <= nj < N:
            if room[ni][nj] == 0:
                room[ni][nj] = 3
                ni += di
                nj += dj

            elif room[ni][nj] == 1:
                break

    blind = 0
    for i in range(N):
        for j in range(N):
            if room[i][j] == 0:
                blind += 1
    print("#{} {}".format(tc, blind))
