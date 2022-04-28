import sys
sys.stdin = open('sample_input.txt')

def DFS(si, sj, cnt, num):
    print(cnt, num)
    # 6번 돌면 종료 한다.
    if cnt == 6:
        temp.add(num)
        return

    # 하상좌우 탐색
    for k in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        ni = si + k[0]
        nj = sj + k[1]

        # 범위 안에 든 좌표만 탐색한다.
        if 0 <= ni < 4 and 0 <= nj < 4:
            DFS(ni, nj, cnt+1, num+str(arr[ni][nj]))


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    # 좌표를 보내서 사방으로 가지를 뻗으며 6번 반복한다.
    cnt = 0
    temp = set()
    for i in range(4):
        for j in range(4):
            DFS(i, j, 0, str(arr[i][j]))

    print('#{} {}'.format(tc, len(temp)))

