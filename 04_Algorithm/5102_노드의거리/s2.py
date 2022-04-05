import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())

def BFS(temp, visited, s):

    # 현재 노드 queue 에 담기
    queue.append([s])

    visited[s] = True
    cnt = 0

    while queue:
        v = queue.pop(0)
        print(v)
        arr = []
        for j in v:
            if j == G:
                return print("#{} {}".format(tc, cnt))

            for i in temp[j]:
                if not visited[i]:
                    arr.append(i)
                    visited[i] = True

        queue.append(arr)

        if not arr:
            return print("#{} {}".format(tc, 0))

        # cnt 는 모든 동작을 끝내고 +1 하는게 국룰이다~
        cnt += 1

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))

    temp = [[] for _ in range(V+1)]

    for i in graph:
        temp[i[0]].append(i[1])
        temp[i[1]].append(i[0])

    # print(temp)

    visited = [False] * (V+1)
    queue = []
    BFS(temp, visited, S)