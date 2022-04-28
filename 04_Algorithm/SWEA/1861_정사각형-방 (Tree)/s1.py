import sys
sys.stdin = open('input.txt')

T = int(input())

def connect(arr, edge):

    r = c = 0
    # 상우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for y in range(N):

        for x in range(N):
            temp = []
            for i in range(4):
                nr = y + dr[i]
                nc = x + dc[i]

                if 0 <= nr < N and 0 <= nc < N:
                    edge[arr[y][x]].append(arr[nr][nc])

        # print(edge)
    return edge

def BFS(a, s):
    # 시작은 1번방부터 계산
    queue.append([s])
    visited[s] = True
    # 1번과 연결된 방 중 1차이가 나는 방이 있는지 확인한다.
    for i in range(1, (N**2+1)):
        cnt = 0
        while queue:
            v = queue.pop()
            for j in v:
                if not visited[j] and i + 1 == j:
                    queue.append(j)
                    cnt += 1
            print(queue)

for tc in range(1, T+1):

    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    edge = [[] for _ in range(N**2 + 1)]

    # 연결상태
    a = connect(arr, edge)
    # [[], [[2, 3]], [[4, 1]], [[1, 4]], [[2, 3]]]
    print('a :',a)
    visited = [False] * (N**2 + 1)
    queue = []
    BFS(a, 1)

    # [9, 3, 4],
    # [6, 1, 5],
    # [7, 8, 2]]