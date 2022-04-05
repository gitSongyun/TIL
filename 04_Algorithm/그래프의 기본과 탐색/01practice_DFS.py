# 연습문제 1번
# 2022-04-01

def DFS(s):
    global stack, cnt

    visited[s] = True

    # 종료조건, 모든 정점을 방문 했을 때
    if len(stack) == 7:
        return

    stack.append(s)

    for v in graph[s]:
        if not visited[v]:
            visited[v] = True
            DFS(v)


N = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

graph = [[] * 8 for _ in range(8)]

for i in range(0, len(N) - 1, 2):
    graph[N[i]].append(N[i + 1])
    graph[N[i + 1]].append(N[i])

stack = []
visited = [False] * 8
cnt = 0
DFS(1)
print(*stack)

# graph = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
