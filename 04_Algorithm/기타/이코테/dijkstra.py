"""
우선순위 큐 사용시
(거리, 노드) 값을 넣는데, 거리를 기준으로 넣어야, 작은 값이 나오게 된다. 
""" 
### 우선순위 큐를 위해 heaq 자료구조 이용
# import sys
# import heapq
# INF = int(1e9)
# start = 1
# # 노드 갯수
# n = 7
# distance = [INF] * (n+1)
# graph = list(map(int, input().slice()))

# heapq으로 queue의 원리를 생각하면 된다. 
# 현재 노드와 현재 노드의 비용 초기화
# 현재 노드와 연결된 다른 노드 탐색
# 그 인접노드가 가진 거리값과 경유해서 간 거리를 비교해서 작은 값을 갱신한다. 
# 탐색중인 루트의 비용이, 기존의 비용보다 크다면 컨티뉴

# def dijkstra(start):
#     distance[start] = 0
#     q = []
#     heapq.heappush(q, (0, start))

#     while q:
#         dist, now = heapq.heappop(q)

#         if distance[now] < dist:
#                 continue
        
#         for i in graph[now]:
        
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))


# dijkstra(start)

#---------------------------------------------------------------------------
### 전보
# import heapq

# def dijkstra(start):
#     distance[start] = 0
#     q = []
#     heapq.heappush(q, (0, start))

#     while q:
#         dist, now = heapq.heappop(q)

#         if distance[now] < dist:
#             continue
            
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0])) 

# INF = int(1e9)
# # N : 도시갯수, M : 통로 갯수, C : 출발 도시
# N, M, C = 3, 2, 1
# #  1 도시에서 2도시 까지 4의 시간 걸림
# cities = [[1, 2, 4], [1, 3, 2], [2, 3, 4], [3, 1, 2]]

# graph = [[] for _ in range(N+1)]
# distance = [INF] * (N+1)
# for city in cities:
#     a, b, c, = city
#     graph[a].append((b, c))


# dijkstra(2)

# print(distance)
#---------------------------------------------------------------------------
### 미래 도시
INF = int(1e9)

def floyd(start):
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    for i in graph:
        print(i)
    return graph
N, 경로갯수 = 5, 7

connect_comp = [[1, 2],[1, 3],[1, 4], [2, 4],[3, 4],[3, 5],[4,5]]

# k를 거쳐 x로
k, x = 4, 5

graph = [[INF] * (N + 1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        if i == j:
            graph[i][j] = 0

for a, b in connect_comp:
    graph[a][b] = 1
    graph[b][a] = 1

result = graph[1][k] + graph[k][x]

floyd(1)
print(graph[1][k] + graph[k][x])