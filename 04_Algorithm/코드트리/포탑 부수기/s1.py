from collections import deque


# 1. 공격자 선정
def find_attacker():
    minV = int(1e9)
    maxT = 0
    minX, minY = 0, 0
    for summ in range(N + M - 2, -1, -1):
        for j in range(M):
            i = summ - j
            if not (0 <= i < N): continue
            if maps[i][j] == 0: continue
            # 약한애 찾기
            if minV > maps[i][j]:
                minV = maps[i][j]
                maxT = lastAttack[i][j]
                minX, minY = i, j
            # 공격력이 같고, 더 최근에 공격한 애라면 갱신
            if minV == maps[i][j] and maxT < lastAttack[i][j]:
                minV = maps[i][j]
                maxT = lastAttack[i][j]
                minX, minY = i, j

    underAttack[minX][minY] = True

    return [minX, minY]

    pass


# 2. 타겟 선정
def find_target():
    global atk
    # 공격력 높고, 공격한지 오래된, 애의 좌표 x, y
    maxV, minT, maxX, maxY = -1, int(1e9), 0, 0
    for summ in range(0, N + M - 1):
        for j in range(0, M):
            i = summ - j
            if not (0 <= i < N): continue

            if maps[i][j] == 0: continue

            if maxV < maps[i][j]:

                maxV, minT, maxX, maxY = maps[i][j], lastAttack[i][j], i, j
                continue
            elif maxV == maps[i][j] and minT > lastAttack[i][j]:

                maxV, minT, maxX, maxY = maps[i][j], lastAttack[i][j], i, j

    return [maxX, maxY]


# 레이저
def raserAtc(atk, tgt):
    canRaser = True
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[atk[0]][atk[1]] = True
    come = [[None for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append([atk[0], atk[1]])
    # 우하좌상
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    while q:
        x, y = q.popleft()

        for d in dirs:
            nx = (x + d[0] + N) % N
            ny = (y + d[1] + M) % M

            if maps[nx][ny] == 0: continue
            if visited[nx][ny]: continue
            visited[nx][ny] = True
            come[nx][ny] = [x, y]
            q.append([nx, ny])

    # 타겟에 도달 못했을 경우 False 리턴
    if not visited[tgt[0]][tgt[1]]:
        return False


    x, y = tgt
    while x != atk[0] or y != atk[1]:
        power = maps[atk[0]][atk[1]] // 2
        if x == tgt[0] and y == tgt[1]:
            power = maps[atk[0]][atk[1]]
        maps[x][y] = attack(x, y, power)
        x, y = come[x][y]

    return True


# 포탄 공격
def bombAtc(atk, tgt):
    # print('포탄공격')
    # 범위 지정
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            nx, ny = (tgt[0] + dx + N) % N, (tgt[1] + dy + M) % M
            if nx == atk[0] and ny == atk[1]: continue

            # 공격력 정하기
            power = maps[atk[0]][atk[1]] // 2
            if nx == tgt[0] and ny == tgt[1]: power = maps[atk[0]][atk[1]]
            # 공격하기
            maps[nx][ny] = attack(nx, ny, power)


# 공격 실행
def attack(x, y, power):
    underAttack[x][y] = True
    return max(0, maps[x][y] - power)


def isFinish():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0:
                cnt += 1
    return cnt == 1


N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
lastAttack = [[0] * M for _ in range(N)]

for i in range(1, K + 1):
    # 포탑 하나만 남았다면 break
    if isFinish():
        break
    underAttack = [[False for _ in range(M)] for _ in range(N)]
    atk = find_attacker()
    tgt = find_target()

    # 공격자 버프
    maps[atk[0]][atk[1]] += N + M
    # 공격자 공격 턴 갱신
    lastAttack[atk[0]][atk[1]] = i

    # 레이저 공격 시도
    if not raserAtc(atk, tgt):
        # 실패시, 포탄 공격 시도
        bombAtc(atk, tgt)
    # print('공격 후')
    # for i in maps:
    #     print(i)
    # 포탑 휴식
    for i in range(N):
        for j in range(M):
            # 공격에 가담되지 않은 포탑인 경우
            if (not underAttack[i][j] and maps[i][j] != 0):
                maps[i][j] += 1
    # print('휴식후')
    # for i in maps:
    #     print(i)

ans = 0
for i in range(N):
    for j in range(M):
        if ans < maps[i][j]:
            ans = maps[i][j]
# for l in lastAttack:
#     print(l)
print(ans)