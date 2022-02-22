# 4871_그래프_경로 풀이
# 2022-02-22
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int,input().split())) # V = 노드 수 , E = 간선 갯수
    node = [[0] * (V+1) for _ in range(V+1)] # 연결된 노드를 표시할 2차원 배열 생성

    # 배열 node의 인덱스
    for _ in range(E):
        r, c = map(int,input().split()) # ex) 1번 4번 노드가 연결되어있다면 node[1][4] = 1
        node[r][c] = 1

    start, goal = list(map(int,input().split())) # 시작점, 도착점

    visited = [False] * (V+1) # 해당 번호의 노드를 방문했는지 체크하는 리스트
    stack = [] # 현재 경로 및 지나온 경로 저장
    stack.append(start) # 시작점 입력
    p = start
    while stack:  # 지나온 경로를 하나 씩 pop하면서 최종적으로 빈 스택이 되면 종료
        # print(stack)
        p = stack[-1]
        for i in range(1, V + 1):

            if node[p][i] == 1:  # 만약 현재 노드와 연결된 다른 노드가 있다면 움직일 것이다.
                node[p][i] = 0   # 방문한 곳을 없애기 위해 0으로 만들고,
                p = i  # 1       # 이제 이 i를 행 인덱스로 사용하여 다시 찾아 나선다.
                stack.append(i)  # stack [1]
                break

            elif i == V: # 끝까지 갔는데 못찾았을 때, stack에서 pop을 한다.
                stack.pop()

        if p == goal: # 만약 도달한 노드가 goal 이라면 while문 종료하겠다.
            break

    if p == goal:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))
