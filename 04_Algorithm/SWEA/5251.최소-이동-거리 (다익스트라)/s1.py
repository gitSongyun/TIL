# 5251_최소이동거리
# 2022-04-05

import sys

sys.stdin = open('sample_input.txt')


def DIJKSTRA(S, p):
    D[S] = 0  # 시작점의 가중치를 0으로 만든다.

    # 노드의 갯수 만큼 반복한다.
    for _ in range(0, N + 1):
        m_idx = -1  # 최소 인덱스 초기화
        mmin = INF  # 최소값 무한대로 초기화

        for i in range(N + 1):
            # i번 노드가 방문하지 않은 곳이고, 가중치가 mmin 보다 작다면
            if not visited[i] and D[i] < mmin:

                # 가중치를 D[i]로 갱신하고
                mmin = D[i]
                # m_idx 를 i로 바꾼다.
                m_idx = i

        visited[m_idx] = True

        for j in range(N + 1):
            if p[m_idx][j] and not visited[j]:
                D[j] = min(D[j], D[m_idx] + p[m_idx][j])


T = int(input())

for tc in range(1, T + 1):
    N, E = list(map(int, input().split()))  # N = 목표, E = 간선 갯수
    arr = [list(map(int, input().split())) for _ in range(E)]
    path = [[0] * (N + 1) for _ in range(N + 1)]

    INF = 1e10

    # 인접행렬 생성
    for s, e, w in arr:
        path[s][e] = w  # s -> e 로 가는데  w의 비용이 든다.
    # map = [[0, 1, 6], [0, 0, 1], [0, 0, 0]]

    visited = [False] * (N + 1)
    D = [INF] * (N + 1)  # 가중치를 담을 리스트
    DIJKSTRA(0, path)

    print('#{} {}'.format(tc, D[-1]))