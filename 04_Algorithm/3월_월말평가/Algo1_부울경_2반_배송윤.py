T = int(input())

for tc in range(1, T+1):
    # N : 농장의 크기 , M : 토끼 수
    N, M = list(map(int, input().split()))

    # 농장 생성
    farm = [[0]*N for _ in range(N)]

    # 방향 설정 (상하좌우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]


    for i in range(M):

        # 행, 열, 이동방향, 점프거리
        r, c, d, j = list(map(int, input().split()))

        # 시작위치 1로 만들기
        farm[r][c] = 1

        a = 0
        while True:
            # 점프 후 좌표
            nr = r + dr[d] * j * a
            nc = c + dc[d] * j * a

            # 범위를 벗어나면 break
            if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
                break

            # 범위 내에 있다면 착지 한 곳을 1로 만들고 다시 점프
            else:
                a += 1
                farm[nr][nc] = 1

    # 피해 입은 구역 계산
    ans = 0
    for r in range(N):
        for c in range(N):
            if farm[r][c] == 1:
                ans += 1

    print("#{} {}".format(tc, ans))