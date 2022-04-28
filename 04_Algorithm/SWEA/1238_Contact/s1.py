# 1238_contact
# 2022-03-17

import sys
sys.stdin = open('input.txt')

T = 10

def BFS(ch, s):

    # 시작 당번을 list 형태로 queue에 담는다.
    queue.append([s])
    # 연락했다고 표시한다.
    visited[s] = True

    while queue:
        # 현재 레벨에 있는 사람
        v = queue.pop(0)
        temp = []
        # v에는 같은 레벨의 노드들이 리스트 형태로 들어가 있다.
        for k in v:
            # k번 사람과 연결된 사람을 j에 넣고
            for j in ch[k]:
                # 처음 연락하는 사람이라면 temp에 넣어두고, 다 연락이 되면 queue에 append 한다.
                if not visited[j]:
                    temp.append(j)
                    visited[j] = True

        # 만약 현재 레벨의 사람과 연결된 사람이 없다면 현재 레벨의 사람들 중 가장 높은 번호를 출력한다.
        if not temp:
            return print("#{} {}".format(tc, max(v)))

        queue.append(temp)

for tc in range(1, T+1):

    # e : 간선 갯수, s : 시작 당번
    e, s = list(map(int, input().split()))
    # 연결 상태
    edge = list(map(int, input().split()))

    # 누가 누구와 연락이 가능한지 인덱스와 원소로 대응시킴
    ch = [[] for _ in range(101)]
    for i in range(0, e, 2):
        ch[edge[i]].append(edge[i+1])

    # BFS에서 활용할 queue
    queue = []
    # 인원은 최대 100명
    visited = [False] * 101
    BFS(ch, s)



