import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    # N: 도시 크기, M : 한 집이 지불 가능한 비용
    N, M = list(map(int, input().split()))
    # 지도 입력
    city = [list(map(int, input().split())) for _ in range(N)]


    dr =
    # 영역 만들기
    for i in range(N):
        for j in range(N):

            for k in range(N+1):


    # 집의 좌표를 찾는다.
    # house = list()
    # for i in range(N):
    #     for j in range(N):
    #         if city[i][j] == 1:
    #             house.append([i, j])