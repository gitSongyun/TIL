import sys
sys.stdin = open('input.txt')

def DFS(adj,start,visited):
    global cnt
    visited[start] = cnt
    
    for i in adj[start]:
        if visited[i] == 0:
            cnt += 1
            DFS(adj,i,visited)

   

N, M, S = map(int, input().split())
visited = [0] * (N+1)
adj= [[] for _ in range(N+1)]
cnt = 1
# 연결 상태 정의
for i in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
    
for i in range(N+1):
    adj[i].sort()

DFS(adj, S, visited)
# start 와 연결된 가작 작은수를 골라 방문처리 한다. 

for i in range(1, N+1):
    print(visited[i])

    