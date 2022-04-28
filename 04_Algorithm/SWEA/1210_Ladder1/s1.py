import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):
    N = int(input())
    temp=[]

    # 2차원 행렬로 받아오기
    for _ in range(100):
        temp.append(list(map(int, input().split())))


    # 문제 대로 행,열을 뒤집어서 정렬
    for i in range(100):
        for j in range(i, 100):
            temp[j][i], temp[i][j] = temp[i][j], temp[j][i]


    dr = [0, -1, 1] # x축
    dc = [-1, 0, 0] # y축

    # 100X100 행렬에서 2 인 위치를 찾아내고
    # 거슬러 올라가야 한다.
    # 위로 올라가다가 좌 or 우에 1이 있다면 dr[1] , dr[2] 를 쓴다.
    # 현재 위치도 설정 해야 할듯

    dir = [[0], 99]
    for x in range(100):
        if temp[x][99] == 2:
         dir[[0][0]] = x

    # dir = [57, 99]

    올라가는 과정
    temp[x][y]에서 y가 0이 되면 반복문 중단
    y = dir[1] # 99
    while y > 0:

        # 좌 우모두 0이라면
        if not temp[dir[0] + 1][dir[1]] and temp[dir[0] - 1][dir[1]]:
           dir[1] += dc[0]

        # 좌 또는 우가 범위에 벗어나지 않고, 1이 있다면,
        # 어디에 1이 있는지 찾고, 그곳으로 움직인다.
        if temp[dir[0] + 1][dir[1]]>=0 and temp[dir[0] - 1][dir[1]]:








