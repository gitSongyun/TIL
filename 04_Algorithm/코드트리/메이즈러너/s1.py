import sys
sys.stdin = open('input.txt')

# 1. 참가자 이동
def move_player():
    # 참가자 별로
    for i in range(M):


        if i in goal:
            continue

        # 행이 다른 경우,
        if players[i][0] != exits[0]:
            p_x, p_y = players[i]
            # 출구보다 위에 있다면 아래로 이동
            if exits[0] > p_x:
                p_x += 1
            # 출구보다 아래에 있다면 위로 이동
            else:
                p_x -= 1
            if maze[p_x][p_y] == 0:
                players[i] = [p_x, p_y]
                exits[2] += 1

                if p_x == exits[0] and p_y == exits[1]:
                    goal.append(i)
                continue


        # 열이 다른 경우
        if players[i][1] != exits[1]:
            p_x, p_y = players[i]
            # 출구보다 왼쪽 있다면 오른쪽으로 이동
            if exits[1] > p_y:
                p_y += 1
            # 출구보다 오른쪽에 있다면 왼쪽 이동
            else:
                p_y -= 1
            if maze[p_x][p_y] == 0:
                players[i] = [p_x, p_y]
                exits[2] += 1
                if p_x == exits[0] and p_y == exits[1]:
                    goal.append(i)
                continue
# 2. 사각형 찾기
def find_sq():
    # 박스를 좌상단 부터 탐색,
    # 박스 사이즈를 2부터 탐색
    global sq
    for size in range(2, N+1):
        # print('출구', exits)
        # print('size', size)
        # bx, by = 사각형 좌상단 꼭짓점
        for bx in range(1, N - size +2):
            for by in range(1, N - size +2):
                # 사각형 우하단 꼭짓점
                nbx = bx + size - 1
                nby = by + size - 1
                # print('좌상단', bx, by, '우핟단', nbx, nby, '출구', exits[0], exits[1])
                # 출구가 사각형 범위 안에 없다면
                if not (bx <= exits[0] and exits[0] <= nbx and by <= exits[1] and exits[1] <= nby):

                   continue

                # 범위 안에 있다면, 플레이어가 한 명이상 존재 하는지 확인
                in_square = False
                for p in players:

                    px = p[0]
                    py = p[1]
                    if (bx <= px and px <= nbx and by <= py and py <= nby):
                        # 출구에 있는 사람이 아닐때
                        if not (exits[0] == px and exits[1] == py):
                            in_square = True

                if in_square:
                    sq = [bx, by, size]
                    # print('사각형 정보', sq)
                    return

# 3. 사각형 회전하기
def rotate():
    tmp_maze = [[0]*(N+1) for _ in range(N+1)]

    # 사각형 안의 벽 감소
    for i in range(sq[0], sq[2]+sq[0]):
        for j in range(sq[1], sq[2]+sq[1]):
            if maze[i][j] != 0:
                maze[i][j] -= 1


    # 정사각형 90도 회전
    for i in range(sq[0], sq[2]+sq[0]):
        for j in range(sq[1], sq[2]+sq[1]):
            ox = i - sq[0]
            oy = j - sq[1]
            rx = oy
            ry = sq[2] - ox - 1
            tmp_maze[rx+sq[0]][ry+sq[1]] = maze[i][j]

    for i in range(sq[0], sq[2]+sq[0]):
        for j in range(sq[1], sq[2]+sq[1]):
            maze[i][j] = tmp_maze[i][j]





# 4. 플레이어, 출구 회전 후 좌표 갱신
def playerRotate():
    global exits
    for k in range(M):
        if k in goal:
            continue
        px, py = players[k]
        if (sq[0] <= px and px < sq[0] + sq[2] and sq[1] <= py and py < sq[1] + sq[2]):
            ox = px - sq[0]
            oy = py - sq[1]
            rx = oy
            ry = sq[2] - ox - 1
            players[k] = [rx + sq[0], ry + sq[1]]

    if (sq[0] <= exits[0] and exits[0] < sq[0] + sq[2] and sq[1] <= exits[1] and exits[1] < sq[1] + sq[2]):
        ox = exits[0] - sq[0]
        oy = exits[1] - sq[1]
        rx = oy
        ry = sq[2] - ox - 1
        exits[0] = rx + sq[0]
        exits[1] = ry + sq[1]
        for g in goal:
            players[g] = [rx + sq[0], ry + sq[1]]

    pass
N, M, K = map(int, input().split())
maze = [[0 for _ in range(N+1)]]
for _ in range(N):
    maze.append([0]+list(map(int, input().split())) )
# print(maze)
# maze = [list(map(int, input().split())) for _ in range(N)]
# 정사각형 좌표, 크기
sq = [0, 0, 0]
# 참가자의 좌표 리스트
players = [list(map(int, input().split())) for _ in range(M)]
# 출구 좌표, 이동 거리
exits = list(map(int, input().split())) + [0]

goal = []


# K번 반복
for i in range(K):
    move_player()
    is_all_es = True
    for i in range(M):
        if not (players[i][0] == exits[0] and players[i][1] == exits[1]):
            is_all_es = False
    if is_all_es: break
    find_sq()
    rotate()

    playerRotate()




print(exits[2])
print(exits[0], exits[1])