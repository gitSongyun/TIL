import sys 
sys.stdin = open('input.txt')

import copy
def dfs(graph, depth):
    global answer
    # 종료조건
    if depth == len(cctv_list):
        answer = min(answer, count_watch(graph)) 
        return
    
    else:
        graph_copy = copy.deepcopy(graph)
        x, y, cctv_type = cctv_list[depth]
        for i in (cctv_dir[cctv_type]):
            
            watch(x, y, graph_copy, i)
            dfs(graph_copy, depth+1)

            graph_copy = copy.deepcopy(graph)
        


def watch(x, y, graph_copy, direction):
    for i in direction:
        nx, ny = x, y   
        while True:

            nx += dir[i][0]
            ny += dir[i][1]
            # 범위 안에 든다면 탐색
            if 0<=nx<N and 0<=ny<M:
                # 감시 가능한 경우
                if graph_copy[nx][ny] == 0:
                    graph_copy[nx][ny] = '#'
                # 벽을 만나면 종료 감시
                elif graph_copy[nx][ny] == 6:
                    break
            # 범위를 벗어나면 종료
            else: 
                break  
    
    pass


def count_watch(graph):
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                count += 1
    
    return count


answer = (1e9)
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cctv_list = []
# 상 우 하 좌
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# cctv 별 방향
cctv_dir = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1],[1, 2], [2, 3], [3, 0]],
    [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    [[0, 1, 2, 3]]
]

# cctv 좌표 찾기 
for i in range(N):
    for j in range(M):
        if 1 <= graph[i][j] <= 5:
            cctv_list.append((i,j, graph[i][j]))


dfs(graph, 0)
print(answer)