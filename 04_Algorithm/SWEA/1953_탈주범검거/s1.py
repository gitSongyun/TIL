import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start, visited, time):
    x, y = start
    q = deque()
    time_q = deque()
    q.append((x,y))
    cnt = 0
    print('시간', time)
    
    while cnt <= time+1:
        if not q:
            break
        x, y = q.popleft()
        cur_type = graph[x][y]

        # 이 반복문에서 현재에서 갈 수잇는 방향의 좌표들이 담기게 된다.
        for d in pipes_type[cur_type]:
            nx = x + dir[d][0] 
            ny = y + dir[d][1]
            
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] > 0 and visited[nx][ny] == 0:
                    next_type = graph[nx][ny]
                    # 연결됐는지 확인
                    if can_move[d] in pipes_type[next_type]:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        cnt = visited[nx][ny]
    


T = int(input())
for test_case in range(1, T+1):
    N, M, s_x, s_y, time = map(int, input().split())
    answer = 0
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[s_x][s_y] = 1
    bfs_list = []
    # 상 우 하 좌
    dir = [(-1,0), (0,1), (1,0), (0,-1)]
    
    # 타입 별 이동 방향
    pipes_type = [
        [],
        [0, 1, 2, 3], # 1
        [0, 2], # 2
        [1, 3], # 3
        [0, 1],  # 4
        [1, 2], # 5
        [2, 3], # 6
        [3, 0], # 7
    ]

    # 이어지는지 확인
    can_move = {
        0 : 2,
        1 : 3,
        2 : 0,
        3 : 1,
    }

    # print(graph)
    bfs((s_x, s_y), visited, time)
    
    # print(visited)
    for i in range(N):
        for j in range(M):
             if 0 < visited[i][j] <= time:
                 answer+=1
    print(f'#{test_case} {answer}')
    
    for i in visited:
        print(i)

    print(graph)