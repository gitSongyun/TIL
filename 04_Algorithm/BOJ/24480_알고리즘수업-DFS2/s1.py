# import sys
# sys.stdin = open('input.txt')

# from collections import deque
# def dfs(start, order):
#     stc = deque()
#     visited[start] = order
#     stc.append(start)
    
#     while stc:
#         cur = stc.pop()
#         if visited[cur] == 0:
#             print(cur)
#             visited[cur] = True
#             for i in graph[cur]:
#                 if visited[i] == 0:
#                     visite.append(i)
#                     stc.append(i)
#             print(cur, visite)               
 
#     return visited

# V, E, S = map(int, input().split())

# graph = [[] for _ in range(V+1)]
# visited = [0] * (V+1)
# order = 0
# visite = []
# for _ in range(E):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for i in range(V+1):
#     graph[i].sort(reverse=True)

# dfs(S, order)


# for i in range(1, len(visited)):
    # print(visited[i])

