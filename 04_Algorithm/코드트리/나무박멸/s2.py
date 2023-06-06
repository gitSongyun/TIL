

# 1. 성장 (나무 상하좌우에 몇개의 나무가 있는지 계산)
def grow():
    for i in range(N):
        for j in range(N):
            # 초기화
            empty[i][j] = 0
            tmp[i][j] = 0
            tree_cnt = 0

            if maps[i][j] > 0:
                for k in ((-1, 0), (0, 1), (1, 0), (0, -1)): # 상우하좌
                    nx = i + k[0]
                    ny = j + k[1]
                    if 0<=nx<N and 0<=ny<N:
                        if maps[nx][ny] > 0:
                            tree_cnt += 1
                        if maps[nx][ny] == 0 and remain[nx][ny] == 0:
                            empty[i][j] += 1
                maps[i][j] += tree_cnt

# 2. 번식 (나무 그루수 // 빈칸 만큼 빈칸에 나무가 자란다)
# 이때 제초제가 있는 곳은 제외한다.
def breed():
    for i in range(N):
        for j in range(N):
            # 나무가 있는 좌표이고,
            if maps[i][j] > 0 :
                # 사방탐색
                for k in ((-1, 0), (0, 1), (1, 0), (0, -1)): # 상우하좌
                    nx = i + k[0]
                    ny = j + k[1]
                    # 범위 벗어난다면 건너뛰기
                    if (nx < 0 or N <= nx) or (ny < 0 or N <= ny):
                        continue
                    # 새로운 좌표가 빈곳이고 제초제도 없다면
                    if maps[nx][ny] == 0 and remain[nx][ny] == 0:
                        tmp[nx][ny] += maps[i][j] // empty[i][j]

    for i in range(N):
        for j in range(N):
            maps[i][j] += tmp[i][j]

# 3. 제초제 뿌릴 위치 찾기
# 뿌리면 가장 많이 죽는 위치 찾고,
# 여러개라면 행이 작고 그다음 열이 작은 순서
def find_remove():
    global ans
    # 나무를 찾고, 한방향으로 보내면서 그 자리에 존재하는 나무들의 누적 갯수 저장
    maxx = 0
    max_x, max_y = 0, 0
    for i in range(N):
        for j in range(N):
            # 나무 자리라면
            if maps[i][j] > 0:
                tmp[i][j] = maps[i][j]
                for d in ((-1,-1), (-1, 1), (1, 1), (1, -1)):
                    nx = i + d[0]
                    ny = j + d[1]
                    for _ in range(K):
                        if not is_range(nx, ny):
                            break
                        tmp[i][j] += maps[nx][ny]
                        nx += d[0]
                        ny += d[1]

    for i in range(N):
        for j in range(N):
            if maxx < tmp[i][j]:
                maxx = tmp[i][j]
                max_x, max_y = i, j


    ans += tmp[max_x][max_y]

    return [max_x, max_y]

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N and maps[x][y] > 0

# 4. 제초제 뿌리기
# 해당 위치에서 대각 방향으로 퍼지며
# 빈칸이거나 벽에 닿는다면 거기까지만 퍼짐
# 닿은 곳은 제초제가 C년 만큼 남으며, 자라지 못하는 환경이 된다.
# 만약 새로운 제초제가 뿌려지면 C년 다시 갱신된다.
def do_remove(x, y):

    for i in range(N):
        for j in range(N):
            if remain[i][j] > 0:
                remain[i][j] -= 1

    maps[x][y] = 0
    remain[x][y] = C
    for d in ((-1, -1), (-1, 1), (1, 1), (1, -1)):
        nx = x + d[0]
        ny = y + d[1]
        for _ in range(K):
            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] != -1:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = 0
                    remain[nx][ny] = C
                    break
                maps[nx][ny] = 0
                remain[nx][ny] = C
                nx += d[0]
                ny += d[1]


# 5. 남은 나무 있는지 확인.
def is_tree():
    for i in range(N):
        for j in range(N):
            if maps[i][j] > 0:
                return False
    return True

N, M, K, C = map(int, input().split())                      # 격자크기, 진행년도, 제초제범위, 제초제 생존 년수
maps = [list(map(int, input().split())) for _ in range(N)]  # 맵
remain = [[0 for _ in range(N)] for _ in range(N)]          # 남은 제초제들
empty = [[0 for _ in range(N)] for _ in range(N)]           # 나무 주위 빈칸에 몇갠지 기록
tmp = [[0 for _ in range(N)] for _ in range(N)]             # 성장과 제초제 자리 찾는데 씀
ans = 0

for i in range(M):
    grow()
    breed()
    x, y = find_remove()
    do_remove(x, y)
    # 나무가 존재하지 않는다면 종료

    if is_tree():
        break

print(ans)
