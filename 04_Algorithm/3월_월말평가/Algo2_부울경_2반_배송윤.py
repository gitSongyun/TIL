import sys
sys.stdin = open('input2.txt')

T = int(input())

def BFS(s, buy, sum_1):

    queue.append([s])
    visited[s[0]][s[1]] = True
    print(queue)
    if not queue:
        return sum_1
    v = queue.pop()

    for i in v:
        y = i[0]
        x = i[1]

        temp = []
        for j in ((-1, 0), (0, 1), (1, 0), (0, -1)): # 상우하좌
            ny = y + j[0]
            nx = x + j[1]
            # 새로 탐색할 곳이 방문 하지 않았고, 0이 아니라면

            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx]:
                    if arr[ny][nx] != 0:
                        visited[ny][nx] = True
                        temp.append([ny, nx])
                        sum_1 += arr[ny][nx]
                        
                    elif arr[ny][nx] == 0:
                        continue
    # print()
    queue.append(temp)
    # print(queue)
    # print(sum_1)


for tc in range(1, T+1):

    N = int(input()) # 격자 크기

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False]*N for _ in range(N)]
    queue = []
    buy = []

    for i in range(N):
        for j in range(N):
            sum_1 = arr[i][j]
            BFS([i, j], buy, sum_1)
            # print(sum_1)
    # 좌표를 보내서 델타탐색 후 방문 여부를 확인한다.
    # 방문하지 않거나 0이 아니라면 그 좌표와 누적합을 buy에 넣는다.
    # 탐색 한 곳이 방문을 했거나, 0이면 새로운 방향으로 다시 탐색
    # 만약 모든 델타 탐색 결과 방문할 곳이 없으면 종료