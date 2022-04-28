import sys

sys.stdin = open('sample_input.txt')

# 이동경로의 경우의 수를 순열로 조회
def pick(n, picked, topick):
    global ans

    if topick == 0:
        ans.append(picked[:])
        return picked[:]

    for i in range(1, n):
        if i not in picked:
            picked.append(i)
            pick(n, picked, topick-1)
            picked.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = []    # 순열을 담을 리스트
    sol = 9999  # 최소값을 찾기 위한 변수
    pick(N, [], N-1)

    print(ans)
    for i in ans:
        # 새로운 경우의 수가 올 때마다 r과 배터리 소모값을 0으로 초기화
        r = 0       # 현재위치
        ssum = 0    # 배터리 소모량

        for j in i: # 다음위치
            print(i)
            # 누적 배터리 소모량
            ssum += arr[r][j]  # r에서 j로 이동한다는 의미,
            r = j              # 현재 위치를 j로 갱신

        ssum += arr[r][0]      # 사무실로 돌아온다.

        # 최소값을 갱신한다.
        if ssum <= sol:
            sol = ssum

    print("#{} {}".format(tc, sol))






