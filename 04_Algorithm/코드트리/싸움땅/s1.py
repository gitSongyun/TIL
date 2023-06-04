import sys
sys.stdin = open('input.txt')

from collections import deque
def simulate(i):
    print('-----------------------')
    print(f'{i+1}라운드 시작')
    print('##############')
    print(people)

    print('맵 현황')
    for i in graph:
        print(i)
    print('##############')
    # 사람 순서대로 반복
    for p_num in range(1, m+1):
#         # print(f'{p_num}번 사람 이동 시작')
        x, y = people[p_num]['pos']
        d = people[p_num]['dir']
        s_info = people[p_num]['stat']
        
        # 해당 방향으로 일단 이동
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        # 이곳이 범위 밖이라면 정반대 방향으로 다시 이동
        if (0 > nx or nx >= n) or (0 > ny or ny >= n):
            d = (d+2)%4
            people[p_num]['dir'] = d
            nx = x + dir[d][0]
            ny = y + dir[d][1]
        
        # 사람 있는지 체크 (res에 기존 사람의 번호가 리턴된다면 )
        res = check(nx, ny)
#         # print('사람 유무 확인 결과', res)
        if res:
            # 싸운다.
#             # print(f'{p_num}번 사람 맞짱뜬다.')
            fight(p_num, res, (nx, ny))
            
        else:
# #           # print('좌표', nx, ny, '사람', p_num)
            getgun((nx, ny), p_num)
            people[p_num]['pos'] = [nx, ny]

#     # print('현황')
#     # print(people)
#     # print('점수현황', point)
    pass

def fight(now, other, position):
    # print(f'싸움시작 이동하는자: {now} vs 상대: {other} ')
    # 두 사람의 인덱스가 필요하다.
    # 진사람은 총을 두고 이동 시킨다.
    winner = loser = 0
    x, y = position
    # 두 사람의 종합스탯을 비교해 누가 이기는지 판별
    if people[now]['stat'][2] > people[other]['stat'][2]:
        winner = now
        loser = other
    
    elif people[now]['stat'][2] < people[other]['stat'][2]:
        winner = other
        loser = now

    # 만약 같은 경우, 초기 스탯을 비교해 승자 패자 나눈다.
    else:
        if people[now]['stat'][0] > people[other]['stat'][0]:
            winner = now
            loser = other
        else:
            winner = other
            loser = now
    # print(people)
    # print(f'승자: {winner}, 패자: {loser}')

    # print('계산전',point)
    # 이긴 사람은 둘 스탯의 차이 만큼 포인트 얻는다.
    point[winner] = abs(people[now]['stat'][2] - people[other]['stat'][2])
    # print('계산후',point)


    # 진 사람은 그 자리에 총을 두고, 본인 방향으로 한번 더 이동 하고

    if type(graph[x][y]) == int:
        graph[x][y] = [graph[x][y]]
    graph[x][y].sort()

    loser_gun = 0
    if people[loser]['stat'][1] > 0:
        # 현재 총의 능력치
        loser_gun = people[loser]['stat'][1]
        graph[x][y].append(loser_gun)
        # 능력치 초기화
        people[loser]['stat'][1] = 0

    # while (사람 없는 곳 찾을 때 까지)
    while True:
        d = people[loser]['dir']
        dx = x + dir[d][0]
        dy = y + dir[d][1]
        # 만약 범위를 벗어난다면
        res = check(dx, dy)
        if (0 > dx or dx > n) or (0 > dy or dy > n):
            # 벗어나진 않았지만 그곳에 사람이 있는 경우
            # 사람이 없는 방향을 찾을때까지 오른쪽 90도 회전하면서 반복
            d = (d+1)%4
            people[loser]['dir'] = d
            continue

        elif res:
            d = (d+1)%4
            people[loser]['dir'] = d
            continue

        # 없는 방향 찾았다면, 위치 갱신 후 getgun
        else:
            people[loser]['pos'] = [dx, dy]
            getgun((dx,dy), loser)
            break

    # 이긴 사람은 그 자리를 차지 하고, 총을 갖는다. getgun
    people[winner]['pos'] = [x, y]
    getgun((x, y), winner)


    pass

def getgun(position, idx):
#     # print(f'{idx}번 플레이어 총줍기 시작')
    x, y = position
#     # print(f'탐색 중인 장소 ({x},{y})')
#     # print(f'{idx}번 정보')
#     # print(people[idx])

    if (0 > x or x >= n) or (0 > y or y >= n):
        return

    if type(graph[x][y]) == int:
        graph[x][y] = [graph[x][y]]
    graph[x][y].sort()

    now_gun = 0
    # 본인의 총이 있는 경우
    if people[idx]['stat'][1] > 0:
        # 현재 총의 능력치
        now_gun = people[idx]['stat'][1]
    
    # 좌표에 총이 없거나 현재 갖고 있는 총이 더 좋다면 그냥 리턴
    if len(graph[x][y]) == 0:
        return
    
    # 해당 좌표의 마지막 총과 자신의 총을 비교
    # 필드 총이 더 좋다면
    new_gun = graph[x][y][-1]
    if new_gun > now_gun:
        # 그 총을 줍고(pop), 스탯 갱신
        # 해당 자리에 다시 총 두고,append 후 갱신
        people[idx]['stat'][1] = new_gun
        people[idx]['stat'][2] = people[idx]['stat'][0] + people[idx]['stat'][1]
        graph[x][y].pop()
        if now_gun != 0:
            graph[x][y].append(now_gun)
        

# 가고자 하는 곳에 사람이 있는지 확인
def check(nx, ny):
    for other in range(1, m+1):
        if [nx, ny] == people[other]['pos']:
            return other

    # 없다면 false 리턴
    return False


# 격자크기, 플레이어 수 , 라운드 
n, m, k = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
point = [0] * (m+1)

# 방향 (상 우 하 좌)
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 플레이어 정보
people = [{
    'pos' : [],
    'dir' : 0,
    'stat' : [],
} for _ in range(m+1)]

for i in range(1, m+1):
    x, y, d, s = map(int, input().split())
    people[i]['pos'] = [x-1, y-1]
    people[i]['dir'] = d
    people[i]['stat'] = [s, 0, s]
# # print('플레이어 정보', people)

for i in range(k):
    simulate(i)

for i in range(1, m+1):
    print(f'{point[i]}', end=' ')
# print(point)

