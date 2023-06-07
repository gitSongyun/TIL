import sys 
sys.stdin = open('input.txt')

from itertools import combinations
from collections import deque
# 격자크기(홀수), 그리드 입력
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
    
visited = [[False for _ in range(N)] for _ in range(N)] # 방문 
grTag = [[0 for _ in range(N)] for _ in range(N)]       # 그룹 번호 기록
grCnt = 0                                               # 그룹이 몇갠지 (조합계산을 위해)
grTile = [0]                                            # 그룹 별 타일 갯수
grSum = [0]                                             # 그룹 별 
grStart = [0]
ans = 0                                                 # 예술점수 계산
tmp = [[0 for _ in range(N)] for _ in range(N)]

# 1. 그룹 만들기
# 접촉한 같은 숫자들 찾기
def grouping():
    global grTile, grSum
    grTile = [0]
    grSum = [0]
    # 초기화
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
            grTag[i][j] = 0
            tmp[i][j] = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                grStart.append([i,j])
                tagging(i, j)
    return

# 태깅
def tagging(x, y):
    global grCnt
    grCnt += 1
    grTile.append(1)
    grSum.append(grid[x][y])
    visited[x][y] = True
    grTag[x][y] = grCnt
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for d in ((-1,0), (0,1), (1,0), (0,-1)): # 상우좌하
            nx = x + d[0]
            ny = y + d[1]
            if is_range(nx, ny):
                if grid[x][y] != grid[nx][ny]: 
                    continue
                grTag[nx][ny] = grCnt
                grTile[grCnt] += 1
                visited[nx][ny] = True
                q.append([nx, ny])
    
    return

def is_range(x, y):
    return 0<=x<N and 0<=y<N and not visited[x][y]

def calcArt():
    # print('grTag----')
    # for g in grTag:
    #     print(g)
    global ans
    tag_Arr = [i for i in range(1, grCnt+1)]
    comb = list(combinations(tag_Arr, 2))


    for i in range(N):
        for j in range(N):
            for d in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx = i + d[0]
                ny = j + d[1]
                if 0<=nx<N and 0<=ny<N and grid[i][j] != grid[nx][ny]:
                    g1, g2 = grTag[i][j], grTag[nx][ny]
                    
                    num1, num2 = grid[i][j], grid[nx][ny]
                    cnt1, cnt2 = grTile[g1], grTile[g2]
                    
                    ans += (cnt1 + cnt2) * num1 * num2
    # # 조합 당 예술점수 계산
    # for c in comb:
    #     for i in range(N):
    #         for j in range(N):
    #             visited[i][j] = False
        
    #     contact = 0 # 접촉면 계산
    #     a, b = c
    #     q = deque()
    #     q.append(grStart[a])
    #     visited[grStart[a][0]][grStart[a][1]] = True
    #     while q:
    #         x, y = q.popleft()
    #         for d in ((-1, 0), (0, 1), (1, 0), (0, -1)):
    #             nx = x + d[0]
    #             ny = y + d[1]
    #             if is_range(nx, ny):
    #                 if grTag[nx][ny] == b:
    #                     contact += 1
    #                 if grTag[nx][ny] == a:
    #                     q.append([nx, ny])
    #                     visited[nx][ny] = True
        
        # print(f'조합{a}, {b}, contact = {contact}')
        # print(grTile, grSum)
        # ans += ((grTile[a] + grTile[b]) * grSum[a] * grSum[b] * contact)
        # print('ans', ans)
    # print(ans)    
    return

def pl_rotate():
    
    # 십자 회전
    half = N//2 # 중심좌표
    for i in range(N):
        for j in range(N):
            if i == half:
                tmp[i][j] = grid[j][i]
            if j == half:
                tmp[i][j] = grid[N-j-1][N-i-1]

    # for g in grid:
    #     print(g)
    # print('----변경후----')
    # for t in tmp:
    #     print(t)

    return

def sq_rotate(x, y, size):
    # 4분면 회전
    for i in range(x, x+size):
        for j in range(y, y+size):
            # print('원래좌표', i, j)
            ox = i - x
            oy = j - y
            rx = oy
            ry = size - ox - 1
            tmp[rx+x][ry+y] = grid[i][j]
            # print('바뀐후 좌표', rx, ry)
    
    
    
    # for i in range(N):
    #     for j in range(N):
    #         grid[i][j] = tmp[i][j]
    #         # tmp[i][j] = 0

    return

for _ in range(4):
    grCnt = 0
    grouping()
    calcArt()
    
    pl_rotate()
    for i in range(0, N, N//2+1):
        for j in range(0, N, N//2+1):
            sq_rotate(i, j, N//2)
    
    for i in range(N):
        for j in range(N):
            grid[i][j] = tmp[i][j]
            


print(ans//2)
