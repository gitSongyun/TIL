# 4871_그래프_경로 풀이
# 2022-02-22
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int,input().split())) # V = 노드 수 , E = 간선 갯수
    node = [[0] * (V+1) for _ in range(V+1)] # 연결된 노드를 표시할 2차원 배열 생성
    for _ in range(E):
        r, c = map(int,input().split()) # ex) 1번 4번 노드가 연결되어있다면 node[1][4] = 1
        node[r][c] = 1
    #[[0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 1, 1, 0, 0],
    # [0, 0, 0, 1, 0, 1, 0],
    # [0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 1],
    # [0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0]]road_2[i] == idx

    start, goal = list(map(int,input().split())) # 시작점, 도착점

    visited = ['F'] * (V+1) # 해당 번호의 노드를 방문했는지 체크하는 리스트
    stack = [] # 현재 경로 및 지나온 경로 저장
    stack.append(start) # 시작점 입력
    while stack: # 지나온 경로를 하나 씩 pop하면서 최종적으로 빈 스택이 되면 종료
        p = stack.pop() # 현재 경로를 stack에서 뽑아와 p에 저장
        visited[p] = 'T' # p번 노드를 방문했다고 저장
        for i in range(V+1): # 노드의 갯수만큼 (1번부터시작) 반복한다.
            if visited[i] == 'F': # 만약 i번 노드에 아직 방문 하지 않았고
                if node[p][i]: # i번 노드와 p번 노드(현재 방문중인 노드)가 연결 되어 있다면
                    stack.append(i) # stack (지나온 경로)에 추가한다.


    if visited[goal] == 'T':
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))

