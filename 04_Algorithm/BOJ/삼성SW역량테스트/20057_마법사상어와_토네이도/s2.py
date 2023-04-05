import sys
sys.stdin = open('input.txt')

answer = 0
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def tornado(answer):
    x = y = N // 2
    # 좌 하 우 상
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    move_cnt = 0
    # 현재 이동중인 방향
    dir = 0
    dist = 1

    graph[x][y] = 0


    while True:
        move_cnt += 1

        # dist만큼 반복
        for i in range(dist):
            nx = x + dx[dir]
            ny = y + dy[dir]
             
            tmp_x = 0
            tmp_y = 0
            # (0,0)에 도착하면 종료
            if nx==0 and ny==-1:
                return
            
            # a, 현재 위치에서 한 칸 더 간 곳에 55%
            # tmp_x = nx + dx[dir] 
            # tmp_y = ny + dy[dir] 
            # if 0<=tmp_x<N and 0<=tmp_y<N:
            #     graph[tmp_x][tmp_y] = graph[nx][ny] * 0.55
        
            
            # 10% (해당 방향으로 한 칸 더가고, 90도 방향 양쪽값에)
            # 홀수 방향(우,좌)이면 짝수방향(상, 하)로 이동
            print('이동 후 좌표', nx, ny)
            for i in [1, -1]:
                nd = (dir+i) % 4
                # 10%
                tmp_x = nx + dx[dir] + dx[nd]
                tmp_y = ny + dy[dir] + dy[nd]
                if 0<=tmp_x<N and 0<=tmp_y<N:
                    graph[tmp_x][tmp_y] += int(graph[nx][ny] * 0.1)
                else:
                    answer += graph[nx][ny] * 0.1
                
                # 7%
                tmp_x = nx + dx[nd]
                tmp_y = ny + dy[nd]
                print(tmp_x, tmp_y)
                if 0<=tmp_x<N and 0<=tmp_y<N:
                    print(int(graph[nx][ny] * 0.07))
                    graph[tmp_x][tmp_y] += int(graph[nx][ny] * 0.07)
                else:
                    answer += graph[nx][ny] * 0.07

                # 1% 
                tmp_x = x + dx[nd]
                tmp_y = y + dy[nd]
                if 0<=tmp_x<N and 0<=tmp_y<N:
                    graph[tmp_x][tmp_y] += int(graph[nx][ny] * 0.01)
                else:
                    answer += graph[nx][ny] * 0.01

                
                # 2%
                tmp_x = nx + dx[nd] * 2
                tmp_y = ny + dy[nd] * 2
                if 0<=tmp_x<N and 0<=tmp_y<N:
                    graph[tmp_x][tmp_y] += int(graph[nx][ny] * 0.02)
                else:
                    answer += graph[nx][ny] * 0.02
                for g in graph:
                    print(g)
                
                

            # 5%
            tmp_x = nx + dx[dir] * 2
            tmp_y = ny + dy[dir] * 2
            if 0<=tmp_x<N and 0<=tmp_y<N:
                graph[tmp_x][tmp_y] = int(graph[nx][ny] * 0.05)
            else:
                answer += graph[nx][ny] * 0.01
            
            x = nx
            y = ny

        # 방향 전환
        dir = (dir+1)%4

        # 방향 전환이 두번 이루어지면 dist 증가
        if move_cnt == 2:
            dist += 1
            move_cnt = 0

    
    
tornado(answer)