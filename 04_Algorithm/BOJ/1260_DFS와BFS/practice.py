from collections import deque

def dfs(graph, s, visited):
    visited_dfs[s] = True
    print(s, end=' ')
    for i in graph[s]:
        if not visited_dfs[i]:
            dfs(graph, i, visited)


def bfs(graph, s, visited):
    queue = deque([s])

    visited[s] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3],
    [1, 5],
    [1, 4],
    [3, 5],
    [2, 4]
]

visited_dfs = [False] * 6
visited_bfs = [False] * 6

dfs(graph, 1, visited_dfs)
print()
bfs(graph, 1, visited_bfs)