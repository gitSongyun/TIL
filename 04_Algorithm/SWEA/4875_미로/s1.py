# 4875_미로
# 2022-02-24
import sys
sys.stdin = open('sample_input.txt')

def FIND(stack):
    global res
    r = stack.pop(0)
    c = stack.pop(0)
    maze[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0<=nr<N and 0<=nc<N:
            if maze[nr][nc] == 3:
                # print(nr, nc)
                res = 1
                return

            if maze[nr][nc] == 0:
                stack.append(nr)
                stack.append(nc)
                maze[nr][nc] = 1
                # print(stack)
                FIND(stack)

T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 미로 크기

    maze = []
    for _ in range(N):
        maze.append(list(map(int,input())))

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                s = [i, j]

    # 상우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 시작점부터 연결된 길의 좌표를 담을 stack
    stack = []

    # 시작점 추가
    stack.append(s[0])
    stack.append(s[1])
    res = 0
    FIND(stack)
    print("#{} {}".format(tc, res))

