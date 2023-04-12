import sys
sys.stdin = open('input.txt')


def dfs(maxx, cnt):
    global answer
    # 최대 사다리 갯수만큼 세웠으면 리턴
    if maxx < cnt:
        return

    # 사다리 돌려보고, true라면 값 갱신
    if simulate():
        answer = min(answer, cnt)
        return


    for i in range(N):
        for j in range(M):
            # 이미 사다리가 놓여져 있다면
            if graph[i][j] != 0:
                continue

            # 현재 위치 기준 왼쪽에 사다리 있는지 확인
            ny = j
            if j > 0:
                ny = j - 1

            nny = j + 1
            nnny = j + 2
            if 0<=ny<M and nnny<M:
                if graph[i][ny] == 0 and graph[i][nny]==0 and graph[i][nnny] == 0:
                    graph[i][j] = 1
                    graph[i][j+1] = 1
                    # print('몇개 세울까',cnt)
                    dfs(maxx, cnt+1)
                    graph[i][j] = 0
                    graph[i][j+1] = 0



    pass

def simulate ():
    # print(graph)
    for i in range(0, M):
        s_x = 0
        s_y = 0
        # 도착점 까지 진행
        while graph[s_x][s_y] != N:
            # print('현재위치',s_x, s_y)

            meet_ladder = False
            # 0이면 아래로 내려감
            if graph[s_x][s_y] == 0:
                s_x += 1
                continue

            # 사다리 만남
            elif graph[s_x][s_y] == 1:
                if s_y < M-1 and graph[s_x][s_y+1] == 1:
                    s_y += 1

                else:
                    s_y -= 1

            s_x+=1


        # print('시작점', i+1)
        # print('도착점', s_y+1)

        if i != s_y:
            return False

    return True



N, M, H = map(int, input().split())
graph = [[0] * (M) for _ in range(N+1)]
answer  = 4


for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1
    graph[a][b+1] = 1
    # print(graph)

for j in range(M):
    graph[N][j] = N

# 그래프
for i in graph:
    print(i)


for i in range(1, 4):
    dfs(i, 0)

print(answer)