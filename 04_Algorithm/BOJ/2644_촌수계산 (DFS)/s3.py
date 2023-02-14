import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS(x, y):
    graph[x][y] += 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1 
                    
       
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

graph[0][0] = 0
# 하나씩 방문 해가면서 graph 값을 레베롤 바꾼다. 

level = 0

# 0,0에서 출발


BFS(0, 0)

print(graph[N-1][M-1])