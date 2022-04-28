import sys
sys.stdin = open('sample_input.txt')

def BFS(s):

    queue.append([s])

    while queue:
        print(queue)
        v = queue.pop(0)

        temp = []
        for z in v:

            for k in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr = z[0] + k[0]
                nc = z[1] + k[1]

                if 0 <= nr < N and 0 <= nc < N:

                    if maze[nr][nc] == 3:
                        return print('#{} {}'.format(tc, cnt[z[0]][z[1]]))

                    # 만약 길이라면
                    elif maze[nr][nc] == 0:
                        temp.append([nr, nc])
                        cnt[nr][nc] = cnt[z[0]][z[1]] + 1
                        maze[nr][nc] = 1
            queue.append(temp)

    print('#{} {}'.format(tc, 0))

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 미로의 크기

    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j

    visited = [[False] * N for _ in range(N)]
    cnt = [[0] * N for _ in range(N)]
    queue = []
    BFS([si, sj])