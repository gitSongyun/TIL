T = int(input())

for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = [] # 던진 위치에 따라 잡힌 물고기의 수를 담을 list

    # 연못 범위내로 그물을 던질 수 있는 위치 [r, c]
    for r in range(N-K+1):
        for c in range(M-K+1):
            ssum = 0 # 그물에 잡힌 물고기 초기화

            # 우, 하, 좌, 상 으로 움직이며 사각형 생성.
            for l in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                # 그물의 크기 만큼 반복
                for k in range(K):
                    nr = r + l[0] * k
                    nc = c + l[1] * k
                    # 잡힌 물고기들 누적합
                    ssum += arr[nr][nc]

                # 방향 전환 시 위치 갱신
                r = nr
                c = nc

            # 위의 반복문(14번 줄)에서 네 모서리의 물고기들은 중복되어 더해진다.
            # 중복되어 더해진 물고기들을 다시 빼주기 위한 코드
            for a in range(0, K, K-1):
                for b in range(0, K, K-1):
                    ssum -= arr[r+a][c+b]

            # 잡힌 물고기들을 ans 에 append 한다.
            ans.append(ssum)

    # 그 중 최대로 잡힌 물고기의 수를 출력한다.
    print("#{} {}".format(tc, max(ans)))



