import sys
sys.stdin = open('input.txt')

from collections import deque
# 입력 받기
N, M = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

people_list = [[-1, -1] for _ in range(M)]              # 사람들 위치
cvs_list = []                                           # 편의점 위치
time = 0                                                # 현재 시간
visited = [[False for _ in range(N)] for _ in range(N)] # 방문처리
step = [[0 for _ in range(N)] for _ in range(N)]        # 최단거리 기록

for _ in range(M):
    x, y = map(int, input().split())
    cvs_list.append([x-1, y-1])

def bfs(start: object) -> object:
    # 방문, 최단거리 초기화
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
            step[i][j] = 0

    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()
        for i in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            nx = x + i[0]
            ny = y + i[1]
            # 크기를 넘어간 경우 건너뛰기
            if (0 > nx or nx >= N) or (0 > ny or ny >= N):
                continue
            # 이미 방문했거나 갈 수 없는 곳인 경우 건너뛰기
            if visited[nx][ny] or maps[nx][ny] == 2:
                continue
            
            visited[nx][ny] = True
            step[nx][ny] = step[x][y] + 1
            q.append([nx, ny])


def simulate():
    # 각 사람들 이동 시키기
    for p in range(M):
        # 편의점에 도착했거나, 격자 밖이라면 건너뛰기
        if people_list[p] == cvs_list[p] or people_list[p] == [-1, -1]:
            continue
        
        # 격자 안이라면 bfs
        bfs(cvs_list[p])

        x, y = people_list[p]
        min_x, min_y = -1, -1
        min_dist = int(1e9)
        for i in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            nx = x + i[0]
            ny = y + i[1]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny] and min_dist > step[nx][ny]:
                    min_x, min_y = nx, ny
                    min_dist = step[nx][ny]
        
        people_list[p] = [min_x, min_y]
       
    # 다 이동시킨 후, 각자 좌표가 편의점 좌표라면 해당 좌표로는 이동 불가하게 
    for m in range(M):
        if people_list[m] == cvs_list[m]:
            x, y = people_list[m]
            maps[x][y] = 2
        

    # time이 M 이하라면 베이스 캠프 찾는 과정을 실시한다.
    if time > M:
        return
    
    # 이 사람과 가장 가까운 베이스 캠프 찾기
    bfs(cvs_list[time-1])

    min_dist = int(1e9)
    min_x, min_y = -1, -1

    for i in range(N):
        for j in range(N):
            if step[i][j] < min_dist and maps[i][j] == 1:
                min_x, min_y, min_dist = i, j, step[i][j]
    people_list[time-1] = [min_x, min_y]
    maps[min_x][min_y] = 2


def is_end():
    cnt = 1
    for i in range(M):
        if people_list[i] != cvs_list[i]:
            cnt += 1
            break
    return cnt == 1

while True:
    time += 1
    simulate()
    if is_end():
        break
# print(people_list)
print(time)
