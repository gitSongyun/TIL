import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())

def BFS(graph, visited, s):
    queue.append([s])
    visited[s] = True
    cnt = 0

    while queue:
        # 현재 노드
        temp = []

        cnt += 1
        v = queue.pop(0) # v는 리스트 []

        # v에는 같은 레벨의 노드가 들어있다. 따라서 하나씩 꺼내서 다음 레벨의 노드를 찾아야 한다.
        for j in v:
            for i in range(E):

                # 다음 탐색할 노드가 방문하지 않았고, 현재 노드와 연결되어 있다면
                if not visited[graph[i][1]] and j == graph[i][0]:
                    # temp 에 append 한다.
                    temp.append(graph[i][1])
                    # visited 에 방문했다고 표시
                    visited[graph[i][1]] = True

                # 이하동문
                elif not visited[graph[i][0]] and j == graph[i][1]:
                    # queue.append(graph[i][0])
                    temp.append(graph[i][0])
                    visited[graph[i][0]] = True

        # 같은 레벨의 노드를 함께 queue 에 append 한다.
        queue.append(temp)

        # temp 에 골인지점이 있다면 cnt 를 출력한다.
        if G in temp:
            return print("#{} {}".format(tc, cnt))

        # 빈 temp 라면 더 이상 연결 된 곳이 없다는 의미이므로 반복문 종료
        if not temp:
            break

    return print("#{} {}".format(tc, 0))


for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))

    visited = [False] * (V+1)
    queue = []
    BFS(graph, visited, S)




