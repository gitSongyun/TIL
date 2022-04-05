# 1226_미로1
# 2022-03-16

from collections import deque
import sys
sys.stdin = open('input (1).txt')

T = int(input())

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        # x, y : 시작위치
        x, y = queue.popleft()

        # 델타 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 도착점에 도착하면 1을 출력한다.
            if maze[nx][ny] == 3:
                return print('#{} {}' .format(tc, 1))

            # 다음에 탐색할 곳이 길이라면
            if maze[nx][ny] == 0:
                # 1로 만들고
                maze[nx][ny] = 1
                # 그 좌표를 queue 에 append 한다.
                queue.append((nx, ny))

    # queue 가 다 비었는데도 도착점을 못 찾았다면 출구 없음
    return print('#{} {}' .format(tc, 0))

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # 위 아래 왼 오른
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 시작 좌표를 BFS 함수에 보낸다.
    BFS(1, 1)
