import sys
sys.stdin = open('input.txt')

# N: 정점 개수, M: 간선 개수, V: 시작 노드
N, M, V = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]
visited = [False] * N
# dfs(graph, V)

for i in graph:
    i.sort()


# DFS, 한놈씩 조지자
def dfs(v):

    print(graph)

    # 종료조건, 더이상 값이 없을 때
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(V)
