from collections import deque


def solution(maps):
    global answer
    global n, m
    n = len(maps)
    m = len(maps[0])

    # 상우하좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위를 벗어나면 continue
                if nx >= n or ny >= m or nx < 0 or ny < 0:
                    continue
                # 벽이면 continue
                if maps[nx][ny] == 0:
                    continue

                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
        return maps

    answer = bfs(0, 0)
    return -1 if answer[n - 1][m - 1] == 1 else answer[n - 1][m - 1]

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]