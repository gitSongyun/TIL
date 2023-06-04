import sys
sys.stdin = open('input.txt')

from collections import deque

def simulate():
    # 조건1. 베이스캠프를 찾은 사람들은 이동
    print(curr_t)

    for i in range(M):
        # 격자 밖에 있거나 도착했다면 탐색하지 않는다.
        if people[i] == [-1, -1] or people[i] == conv[i]:

            continue

        bfs(conv[i])
        print('step')
        for s in step:
            print(s)
        print('-------------')
        # 탐색, 현재 사람의 위치에서 시작
        px, py = people[i]
        minn = int(1e9)
        min_x = -1
        min_y = -1
        for j in range(4):
            nx = px + dx[j]
            ny = py + dy[j]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] and minn > step[nx][ny]:
                    minn = step[nx][ny]
                    min_x = nx
                    min_y = ny
        people[i] = (min_x, min_y)


    # 편의점에 도착했다면, 방문하지 말라는 의미로 2로 바꿔줌
    for i in range(M):
        if people[i] == conv[i]:
            x = people[i][0]
            y = people[i][1]
            graph[x][y] = 2

    if curr_t > M :
        return

    # 베이스 캠프를 찾아야 한다.
    bfs(conv[curr_t-1])
    minn = int(1e9)
    min_x = -1
    min_y = -1
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                if minn > step[i][j]:
                    minn = step[i][j]
                    min_x = i
                    min_y = j
    graph[min_x][min_y] = 2
    people[curr_t-1] = (min_x, min_y)




# bfs를 돌리면서 최소 거리를 찾는다. (이동이든, 베이스캠프든)
def bfs(start):
    # 방문, 거리 리스트 초기화
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
            step[i][j] = 0

    # bfs탐색
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and graph[nx][ny] != 2:
                    step[nx][ny] = step[x][y] + 1
                    q.append([nx, ny])


def is_end():

    for i in range(M):
        if people[i] != conv[i]:
            return False

    return True


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
conv = []
people = [(-1, -1) for _ in range(M)]
arrive = []
step = [[0] * N for _ in range(N)]
# print(arrive)
visited = [[False] * N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    conv.append((x,y))
print('편의점', conv)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
house = []

curr_t = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i,j))

while curr_t < 10:
    curr_t += 1
    simulate()
    print(people)
    if is_end():

        break
    # for s in step:
    #     print(s)
    # print('-----------------')

print(curr_t)

