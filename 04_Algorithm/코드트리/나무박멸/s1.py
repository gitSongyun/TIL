import sys
sys.stdin = open('input.txt')

from collections import deque

def simulate():
    global answer
    # 빈공간이 몇개 인지
    tmp_map = [[0] * n for _ in range(n)]

    print('시작')
    print('remove_map 현황')
    for r in remove_map:
        print(r)
    print('---------')

    # step1. 나무 성장
    for i in range(n):
        for j in range(n):
            # 그곳이 나무라면 성장 시키기 발동
            if graph[i][j] > 0:
                empty = grow(i,j, 0)
                if remove_map[i][j] == 0:
                    tmp_map[i][j] = empty
    # print('성장끝')
    # print('tmp_map 현황')
    # for r in tmp_map:
    #     print(r)
    # print('---------')
    # #
    # #
    # print('성장끝')
    # print('그래프 현황')
    # for r in graph:
    #     print(r)
    # print('---------')
    #
    # print('tmp_map현황')
    # for t in tmp_map:
    #     print(t)
    # print('---------')
    #
    # print('remove 현황')
    # for t in remove_map:
    #     print(t)
    # print('---------')
    # step2. 번식
    for i in range(n):
        for j in range(n):
            # 제초제 구역이라면, 그 칸 패스
            # if remove_map[i][j] > 1:
            #     continue
            # 나무라면 그 주변 탐색
            if graph[i][j] > 0:
                bunsik(i, j, tmp_map)

    print('번식맵')
    for r in tmp_map:
        print(r)
    print('---------')
    # 번식 완료
    for i in range(n):
        for j in range(n):
            graph[i][j] = graph[i][j] + tmp_map[i][j]

    print('번식끝',graph)
    print('그래프 현황')
    for r in graph:
        print(r)
    print('---------')
    tmp_map = [[0] * n for _ in range(n)]

    # step3. 제초제 탐색
    tot = 0
    t_x = t_y = -1
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                tmp_tot = find_pos(i,j)
                if tot < tmp_tot:
                    tot = tmp_tot
                    t_x , t_y = i, j

    answer += tot
    # tmp_map 초기화


    for i in range(n):
        for j in range(n):
            if remove_map[i][j] > 0:
                remove_map[i][j] -=1
    # 제초제 뿌리기
    remove(t_x, t_y)

    print('제초제 맵')
    for r in remove_map:
        print(r)
    print('---------')


# 성장
def grow(x, y, empty):

    cnt = 0
    # 사방 탐색으로 나무 갯수 센다.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] > 0 :
                cnt += 1

            if graph[nx][ny] == 0 and remove_map[nx][ny] == 0:
                # print(nx, ny)
                empty += 1


    graph[x][y] += cnt

    return empty


# 번식
def bunsik(x, y, tmp_map):
    cnt = tmp_map[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if remove_map[x][y] > 0:
                continue

            elif graph[nx][ny] == 0 :
                tmp_map[nx][ny] += graph[x][y] // cnt

    tmp_map[x][y] = 0



# 제초제 탐색
def find_pos(x, y):
    # 좌 상단 부터
    total = graph[x][y]

    for i in range(4):
        nx, ny = x, y
        for j in range(k):
            nx += dir[i][0]
            ny += dir[i][1]
            if 0<=nx<n and 0<=ny<n:
                # 그 칸이 나무라면
                if graph[nx][ny] > 0:
                    total += graph[nx][ny]
                # 나무가 아니라면 해당 방향 탐색 멈춤
                else:
                    continue
            # 범위를 벗어나면 해당방향 탐색 멈춤
            else:
                break

    return total

# 제초제 뿌리기
def remove(x, y):
    graph[x][y] = 0
    remove_map[x][y] = c
    for i in range(4):
        nx, ny = x, y
        for j in range(k):
            nx += dir[i][0]
            ny += dir[i][1]
            if 0<=nx<n and 0<=ny<n:
                # 그 칸이 벽이 아니라면,
                print('그래프 현황***********************')
                for r in graph:
                    print(r)
                print('---------')
                if graph[nx][ny] != -1:
                    graph[nx][ny] = 0
                    remove_map[nx][ny] = c
                else:
                    break
            # 범위를 벗어나면 해당방향 제초제 멈춤
            else:
                break
    pass

# 크기, 박멸 진행수, 확산범위, 제초제 수명
n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 제초제 현황 맵
remove_map = [[0] * n for _ in range(n)]
answer = 0
# 대각
dir = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
# 사방
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(m):
    simulate()


print(answer)
