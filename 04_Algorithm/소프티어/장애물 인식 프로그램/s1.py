import sys
sys.stdin = open('input.txt')
def DFS(x, y):
    print(graph)
    # 종료조건, 범위를 벗어나면 재귀 종료
    if x <= -1 or x >= N or y >= N or y <= -1:
        return False

    print(x, y)
    # 방문하지 않았다면 탐색
    if graph[x][y] == 1:
        # 방문 처리
        graph[x][y] = 2
        # 위, 오, 아, 왼 순서로
        DFS(x-1, y)
        DFS(x, y+1)
        DFS(x+1, y)
        DFS(x, y-1)
        return True
    return False


# 배열 크기
N = int(input())

# 그래프
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 블록 갯수
result = 0

# 방문 리스트


# 각 위치 DFS 탐색
for i in range(N):
    print(i)
    for j in range(N):
        if DFS(i, j) == True:
            result += 1

print(result)