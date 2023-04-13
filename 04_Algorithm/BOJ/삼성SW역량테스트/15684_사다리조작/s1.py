import sys
sys.stdin = open('input.txt')


def dfs(maxx, idx, cnt):
    global answer
    # 종료조건, 벽을 몇개 세우는지.
    # 0개일땐 시뮬 돌리고 리턴
    if maxx == 0:
        if simulate():
            answer = min(answer, cnt)
        return


    # 1개 세우는데, 벽 2개가 되면 아무것도 안하고 리턴
    if maxx < cnt:
        return
    # 사다리 세울 때 마다 시작
    if simulate():
        answer = min(answer, cnt)

    for j in range(idx, N):
        for i in range(H):
            ny = j - 1
            nyy = j + 1
            nyyy = j + 2
            if ny<0:
                if graph[i][nyy] == 0 and graph[i][nyyy] == 0:
                    dfs(maxx, idx, cnt+1)

    pass

def simulate ():
    # print(graph)
    for i in range(0, M):
        s_x = 0
        s_y = i
        # 도착점 까지 진행
        while graph[s_x][s_y] != N:
            # print('현재위치',s_x, s_y)
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
graph = [[0] * (M+1) for _ in range(N+1)]
answer  = 4


for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1
    graph[a][b+1] = 1

for j in range(M):
    graph[N][j] = N

# 그래프
for i in graph:
    print(i)


for i in range(0, 4):
    dfs(i, 0, 0)

simulate()

print(answer)