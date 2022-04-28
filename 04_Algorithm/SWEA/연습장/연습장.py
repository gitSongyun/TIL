
# 최대힙
def enq(n):
    global last
    last += 1
    tree[last] = n  # 완전이진트리 유지

    # 최대 힙 관리
    c = last  # 새로 추가된 정점을 자식으로
    p = c // 2  # 완전이진트리에서의 부모 정점 번호

    while p > 0 and tree[p] < tree[c]:  # 부모가 있고, 자식의 키 값이 더 크면 교환
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


def deq():
    global last
    tmp = tree[1]  # 루트의 key값
    tree[1] = tree[last]  # 마지막 정점의 키를 루트에 복사
    last -= 1  # 마지막 정점 삭제

    # 부모>자식 규칙 유지
    p = 1
    c = p * 2  # 왼쪽자식노드 번호

    while c <= last:  # 왼쪽 자식이 있으면
        if c + 1 <= last and tree[c] < tree[c + 1]:  # 오른쪽 자식노드가 있고, 오른쪽 자식이 더 크면
            c += 1  # 오른쪽 자식 선택
        if tree[p] < tree[c]:  # 자식의 키값이 더 크면 교환
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2
        else:
            break

    return tmp


# 포화이진트리의 정점번호 1~100
tree = [0] * 101
last = 0  # 마지막 정점 번호


## 부분집합 ##
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)

result = []
for i in range(0, (1<<n)):
    sum = 0
    ans = []
    for j in range(0, n):

        if i & (1 << j):
            sum += int(arr[j])
            ans.append(str(arr[j]))
    if sum == 0:
        result.append(ans)

for i in result:
    print(i)



## 루트, 조상찾기 ##
E = int(input())  # edge 수
arr = list(map(int, input().split()))
V = E + 1         # 정점 수 == 1번부터 V번까지 정점이 있을 때 마지막 정점 번호

# 자식 번호를 인덱스로 부모 번호를 저장
par = [0] * (V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p

print(*par)

# root 찾기
root = 0
for i in range(1, V+1):
    if par[i] == 0:  # par[i]가 0이다 = 부모노드가 없다 = root !
        root = i
        break

print(root)


# 조상찾기
c = 5    # 정점 c의 조상찾기
anc = []
while par[c] != 0:
    anc.append(par[c])
    c = par[c]

print(*anc)


## 다익스트라 ##
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
# 주어지는 그래프 정보 담는 N개 길이의 리스트
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)  # 방문처리 기록용
distance = [INF] * (n+1)   # 거리 테이블용

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드이면서 시작노드와 최단거리인 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작노드 -> 시작노드 거리 계산 및 방문처리
    distance[start] = 0
    visited[start] = True
    # 시작노드의 인접한 노드들에 대해 최단거리 계산
    for i in graph[start]:
        distance[i[0]] = i[1]

    # 시작노드 제외한 n-1개의 다른 노드들 처리
    for _ in range(n-1):
        now = get_smallest_node()  # 방문X 면서 시작노드와 최단거리인 노드 반환
        visited[now] = True        # 해당 노드 방문처리
        # 해당 노드의 인접한 노드들 간의 거리 계산
        for next in graph[now]:
            cost = distance[now] + next[1]  # 시작->now 거리 + now->now의 인접노드 거리
            if cost < distance[next[0]]:    # cost < 시작->now의 인접노드 다이렉트 거리
                distance[next[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('도달 할 수 없음')
    else:
        print(distance[i])