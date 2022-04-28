import sys

sys.stdin = open('algo2_sample_in.txt')


# 조합, 비복원
def pick(n, picked, topick):
    global com
    if topick == 0:
        com.append(picked[::])
        return

    if not picked:
        smallest = 0

    else:
        smallest = picked[-1]

    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            pick(n, picked, topick - 1)
            picked.pop()


def BFS(s, d):
    global com, wall

    # 조합에 따른 1을 제거 한 다음, 탐색을 하면서 최소 거리를 찾아보자
    for a, b in com:
        # 두 개의 벽 제거
        maze[wall[a][0]][wall[a][1]] = 0
        maze[wall[b][0]][wall[b][1]] = 0

        queue = []
        queue.append(s)

        while queue:
            p = queue.pop()

            for v in p:

                temp = []
                for k in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nr = p[0] + k[0]
                    nc = p[1] + k[1]

                    if maze[nr][nc] == 3:
                        break

                    if 0 <= nr < 0 and 0 <= nc < 0:
                        if maze[nr][nc] == 0:
                            d[nr][nc] += d[s[0]][s[1]]
                            temp.append([nr, nc])

                queue.append(temp)



    return d[nr][nc]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 미로의 크기

    maze = [list(map(int, input())) for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    stack = []
    com = []

    # 1의 좌표와 갯수를 파악한다.
    cnt = 0
    wall = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 1:
                cnt += 1
                wall.append([i, j])

            elif maze[i][j] == 2:
                start = [i, j]


    # wall = [[1, 0], [1, 1], [1, 2], [3, 1], [3, 2], [3, 3]]
    # com = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    pick(cnt, [], 2)

    print(BFS(start, dist))

