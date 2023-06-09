from collections import deque


def bfs(start, n, connect):
    cnt = 0
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    # print(visited)
    # 각 노드에 몇 분에 도착했는지 기록
    check_time = [-1 for _ in range(n + 1)]
    check_time[start] = 0
    # print(check_time)
    q = deque()
    q.append(start)

    while q:
        s = q.popleft()

        for next in connect[s]:
            # print('next=', next)
            # print(visited)
            if not visited[next]:
                # print('방문')
                q.append(next)
                visited[next] = True
                check_time[next] = check_time[s] + 1

    return check_time


def solution(n, roads, sources, destination):
    answer = []
    connect = [[] for _ in range(n + 1)]
    result = []
    for r in roads:
        a, b = r
        connect[a].append(b)
        connect[b].append(a)

    res = bfs(destination, n, connect)

    for s in sources:
        result.append(res[s])
    return result