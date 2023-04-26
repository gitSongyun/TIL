import sys
sys.stdin = open('input.txt')

import heapq
INF = int(1e9)
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
distance = [[INF] * (V+1) for _ in range(V+1)]
h = []
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    distance[a][b] = c
    heapq.heappush(h, (c, a, b))

while h:
    # print('힙상태',h)
    dist, start, goal = heapq.heappop(h)
    # print(f'start = {start}, goal = {goal}')

    if start == goal:
        print(dist)
        break

    if distance[start][goal] < dist:
        continue

    for d, g in graph[goal]:
        # print(f'{goal}에서 갈 수 있는 노드 = {g}, 거리값 {d}')
        nd = dist + d
        if nd < distance[start][g]:
            # print(f'{start}에서 {goal}을 거쳐 {g}로 가는데 갱신된 비용 {nd}')
            distance[start][g] = nd
            heapq.heappush(h, (nd, start, g))
    # print('거리값 그래프')
    # for d in distance:
        # print(d)
else:
    print(-1)
# import sys
# sys.stdin = open('input.txt')
#
# def floid():
#     for k in range(V):
#         for i in range(V):
#             for j in range(V):
#                 d[i][j] = min(d[i][j], d[i][k] + d[k][j])
#     pass
#
# INF = int(1e9)
# V, E = map(int, input().split())
# d = [[INF] * V for _ in range(V)]
#
# for i in range(E):
#     a, b, c = map(int, input().split())
#     a-=1
#     b-=1
#     d[a][b] = c
#
# for i in range(V):
#     d[i][i] = 0
#
# floid()
# print(d)
