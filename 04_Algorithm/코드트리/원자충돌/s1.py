import sys
sys.stdin = open('input.txt')

'''
고민 1. 원자의 생성 및 삭제 시 append, pop 로 제거 할 것인가.
       그렇다면, 생성 및 삭제되는 원자의 인덱스가 필요할 듯. 아님 좌표로 찾아도되고
고민 1-1. 그럼, 4개가 생성되면 어펜드만 번 일어나게 되는데... 
해결 1-1. 2차원 배열을 활용해서, 삭제되는 애들은 없애버리면될듯.
'''

# 원자는 자신의 속력만큼 자신의 방향으로 이동
# 이동이 모두 끝나고
# 한칸에 두개 이상의 원자가 있다면 합성 일어남
    # 같은 칸에 있는 원자들의 질량+속력을 모두 합한 하나의 원자로 됨
    # 이 원자는 4개의 원자로 나눠짐
    # 나눠진 원자들은 해당칸에 위치 후 다음과 같이 성질 나뉨
        # 질량 = 합쳐진원자의 질량 // 5
        # 속력 = 속력 합 // 합쳐진 원자 갯수
        # 방향 = 합쳐진 원자의 방향이 상하좌우 중 하나이면 상하좌우, 대각선 방향이면 각각의 방향,
        #        모두 아니면, 대각선 4방향으로 향함.
    # 질량 0 인애는 소멸

# 이동 중의 원자는 합성 아님.

# 격자크기, 원자갯수, 실험시간
N,M,K = map(int, input().split())
grid = [[[] for _ in range(N)] for _ in range(N)]
for i in range(M):
    # 좌표, 질량, 속도, 방향
    x,y,m,s,d = list(map(int, input().split()))
    grid[x-1][y-1].append([m, s, d])


# ↑, ↗, →, ↘, ↓, ↙, ←, ↖
dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

next_grid = [[[] for _ in range(N)] for _ in range(N)]


# 시뮬레이션
def simulate():
    # 이동 후 grid 초기화
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = []

    move()

    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]
    return
# 1. 원자 이동
def move():
    # 원자들 이동
    for i in range(N):
        for j in range(N):
            for atom in grid[i][j]:
                m, s, d = atom
                nx = (i + s* dirs[d][0] + N) % N
                ny = (j + s* dirs[d][1] + N) % N
                next_grid[nx][ny].append((m, s, d))

    # print('이동 후 결과')
    # for i in next_grid:
    #     print(i)
    # 합성 할 건지 탐색
    for i in range(N):
        for j in range(N):
            # 해당좌표에 원자가 두개 이상이면
            if len(next_grid[i][j]) > 1:
                # 합성 실시
                compound(i, j)

    # print('최종 넥스트')

    return
# 2. 합성
def compound(x, y):
    diff_dir = False
    # print('합성 시 좌표')
    # for i in next_grid:
    #     print(i)
    # print(f'{x},{y}에서 합성 일어남')
    sum_mass = sum_speed = 0
    new_dir = [0, 2, 4, 6]              # 일단 사방향으로 저장
    tmp_dir = next_grid[x][y][0][2] % 2
    for atoms in next_grid[x][y]:
        m, s, d = atoms
        sum_mass += m
        sum_speed += s
        # 첫번째 원자의 방향과 다른 종류의 방향이라면
        if tmp_dir != (d % 2):
            diff_dir = True

    sum_mass //= 5
    sum_speed //= len(next_grid[x][y])
    # 서로 다른 종류의 방향이라면 , 대각으로 갱신
    if diff_dir:
        new_dir = [1, 3, 5, 7]

    split(x, y, sum_mass, sum_speed, new_dir)
    return
# 3. 분열
def split(x, y, mass, speed, dir):

    next_grid[x][y] = []

    if mass <= 0:
        return

    for i in range(4):
        next_grid[x][y].append((mass, speed, dir[i]))

    return

for i in range(K):
    simulate()

# print('최종')


ans = 0
for i in range(N):
    for j in range(N):
        if len(grid[i][j]) <= 0:
            continue

        for g in grid[i][j]:
            ans += g[0]
print(ans)
