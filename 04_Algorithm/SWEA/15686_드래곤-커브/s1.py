import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [[0] * 101 for _ in range(101)]

delta = ((0, 1), (-1, 0), (0, -1), (1, 0))

for i in range(N):
    x, y, d, g = list(map(int,input().split()))

    # 현재 위치 1로 바꾸자
    arr[x][y] = 1

    path = [d]
    for j in range(g):
        temp = []
        for k in range(len(path)):
            # 0 ->0, 1 -> 0, 1, 2, 1 -> 0, 1, 2, 1, 2, 3, 2, 1
            # 규칙찾고 temp 에 넣는다.
            temp.append(path[j]  )

        # 세대에 따른 방향전환 리스트
        path.append(temp)

    # 이동 하면서 그 좌표는 1로 바꿔 준다.
    for l in path:
        nx = x + delta[l][0]
        ny = y + delta[l][1]

        # 이동할 좌표가 배열 범위안에 들어오면
        if 0 <= nx < N and 0 <= ny < N:
            arr[nx][ny] = 1

# 사각형 갯수
ans = 0
# 다 바꾸고 나면 네모의 갯수를 찾아야 한다.
# 네모 갯수는 또 어떻게 찾냐 ....
# 현재 좌표 기준 오른쪽, 아래쪽, 오른쪽아래 대각선 3곳의 값을 확인해야 할 듯
for r in range(N-1):
    for c in range(N-1):
        cnt = 0
        if arr[r][c] == 1:
            for o in ((0, 1), (1, 0), (1, 1)):
                nr = r + o[0]
                nc = c + o[1]

                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == 1:
                        cnt += 1

                if cnt == 3:
                    ans += 1



    # 몇 세대 인지에 따라 반복문을 해야 할까?
    # 몇 세대 인지에 따라 방향에 규칙성이 있나?
    # 뭔 규칙성... 안보여....

    # 세대별 방향 (ex d = 0)
    # 0세대 [0]
    # 1세대 [0, 1]
    # 2세대 [0, 1, 2, 1]
    # 3세대 [0, 1, 2, 1, 2, 3, 2, 1]
    # 4세대 [0, 1, 2, 1, 2, 3, 2, 1,
    #       2, 3, 0, 3, 2, 3, 2, 1]

    # d = 1
    # 0세대 [1]
    # 1세대 [1, 2]
    # 2세대 [1, 2, 3, 2]
# 뭔 말이야 이게