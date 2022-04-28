# 연습문제2_BFS
# 2022-04-01
def BFS(s):
    queue = []
    front = -1
    rear = 0

    queue.append([s])
    rear += 1
    print(queue)
    while front <= rear:
        print(front, rear)
        front += 1
        v = queue[front]

        temp = []
        for i in graph[v]:
            if not visited[i]:
                temp.append(i)
                visited[i] = True

        queue.append(temp)
        rear += 1

    print(queue)


N = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

graph = [[] * 8 for _ in range(8)]

for i in range(0, len(N) - 1, 2):
    graph[N[i]].append(N[i + 1])
    graph[N[i + 1]].append(N[i])

stack = []
visited = [False] * 8

BFS(1)

# graph = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
