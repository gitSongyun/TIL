import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    temp = []

    # 2차원 행렬로 받아오기 (100X102)
    # idx error 를 피하기 위해 양쪽 열에 0을 추가한다.
    for _ in range(100):
        temp.append([0] + list(map(int, input().split())) + [0])

    # 위로, 좌우로 움직이겠다.
    dr = [0, -1, 1]  # 좌우
    dc = [-1, 0, 0]  # 상

    # dir = 시작위치, 도착점에서 시작하기 때문에 99번째 행에서 2를 가진 값을 찾는다.
    dir = [99, 0]
    for x in range(102):
        if temp[99][x] == 2:
            dir[1] = x

    # 맨 위행렬로 올라가기 위해 while 을 반복하겠다.
    while dir[0] >= 0:

        # 좌 우모두 0이라면
        if not (temp[dir[0]][dir[1]+1] or (temp[dir[0]][dir[1]-1])):
            # 위로 올라갈게
           dir[0] += dc[0]

        # 1이 오른쪽에 있는지, 왼쪽에 있는지 찾아야 한다.
        # 오른쪽의 값이 1이라면
        if temp[dir[0]][dir[1] + 1]:
            # 0을 만날 때까지 오른쪽으로 움직인다.
            while temp[dir[0]][dir[1] + 1]:
                dir[1] += dr[2]
            # 다리를 다 건넜으면 위로 한칸 올려준다.
            dir[0] += dc[0]

        # 왼쪽 값이 1이라면
        if temp[dir[0]][dir[1] - 1]:
            # 0 을 만날 때 까지 왼쪽으로 움직인다.
            while temp[dir[0]][dir[1] - 1]:
                dir[1] += dr[1]
            # 다리를 다 건넜으면 위로 한칸 올려 준다.
            dir[0] += dc[0]

    # 양옆 열에 0을 추가 했으므로 -1을 해주면 본래 열의 위치를 구할 수 있다.
    print("#{} {}" .format(tc, dir[1]-1))
