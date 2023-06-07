import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

round_cnt = 0    # 라운드 메모
team = []        # 각 팀 좌표 기록, 
team_dir = [None for _ in range(M) ]    # 각 팀 회전 방향 [s, e, 1, 머리인덱스]
visited = [[False for _ in range(N)] for _ in range(N)] # 
dir = ((-1,0), (0, 1), (1, 0), (0, -1))
ans = 0

tag_arr = [[None for _ in range(N)] for _ in range(N)]
tag = 0


# 팀 기록
def findTeam(x, y, cnt, t, no, tag, od):
    t.append([x,y, no, od])

    if cnt >= 2:
        team.append(t)
        return
    
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if in_range(nx, ny):
            if 2<=maps[nx][ny]<=3:
                tag_arr[nx][ny] = [tag, od]
                visited[nx][ny] = True
                if maps[nx][ny] == 1 or maps[nx][ny] == 3:
                    cnt += 1
                findTeam(nx, ny, cnt, t, maps[nx][ny], tag, od+1)
    return 

def in_range(x, y):
    return 0<=x<N and 0<=y<N and not visited[x][y]

# 탐색을 통해 사람 찾는다.
for i in range(N):
    for j in range(N):     
        if not visited[i][j] and maps[i][j] == 1:
            tag += 1
            od = 1
            cnt = 1
            tag_arr[i][j] = [tag, od]
            visited[i][j] = True
            findTeam(i, j, cnt, [], maps[i][j], tag, od)

# for t in tag_arr:
#     print(t)
# 각 팀 방향 기록
for t in range(M):
    team_dir[t] = [len(team[t])-1 , 0, (-1) , 0] # 처음은 꼬리 인덱스, 머리 바로앞 인덱스, 증감, 머리 인덱스 , 방향 바뀌면 머리 인덱스, 꼬리 바로앞, 증감, 머리 인덱스

# 1. 각 팀 이동
def move():
    # 머리 부터 움직임
    for i in range(M):
        s, e, d, h = team_dir[i]
        print(s, e, d, h)
        # 각 팀을 방향대로 움직인다. 
        for k in range(s, e, d):
            print(i, k)
            # 꼬리면 자기 지나간 자리 4로 바꾸자.
            ox, oy, oNo, od = team[i][k]
            if k == s:
                print('꼬리니까 바꿔주자')
                maps[ox][oy] = 4
                for m in maps:
                    print(m)
                tag_arr[ox][oy] = None
    
            nx, ny, nNo, nOd = team[i][k+d]
            print('새좌표', nx, ny)
            team[i][k] = [nx, ny, oNo, od]
            maps[nx][ny] = oNo
            tag_arr[nx][ny] = [i + 1, od]


        x, y, no, od = team[i][h]

        for dr in dir:
            nx = x + dr[0]
            ny = y + dr[1]
            if 0<=nx<N and 0<=ny<N:
                if maps[nx][ny] == 4:
                    team[i][h] = [nx, ny, no, od]
                    maps[nx][ny] = no
                    tag_arr[nx][ny] = [i+1, od]
                            
    return

# 2. 공 던지기
def ball():
    # 공 맞았을 때, 몇 팀인지 봐야 함. 
    global ans
    r = (round_cnt-1) % (4*N) + 1
    # print('현재 라운드',r)
    if r <= N:
        hold = r-1
        for j in range(N):
            if 1<=maps[r-1][j]<=3:
                team_no = tag_arr[hold][j][0] - 1
                team_haad = team_dir[team_no][3]
                ans += (tag_arr[hold][j][1] - team_haad) ** 2
                change_head(team_haad, team_no)

                # ans += (maps[hold][j]) ** 2
                return
        return
    
    elif r <= 2*N:
        hold = r % (N+1)
        for i in range(N-1, -1, -1):
            if 1<=maps[i][hold] <= 3:
                ans += (maps[i][hold]) ** 2
                team_no = tag_arr[i][hold] - 1
                team_haad = team_dir[team_no][3]
                ans += (tag_arr[hold][j][1] - team_haad) ** 2
                change_head(team_haad, team_no)
                return
        return
    
    elif r <= 3*N:
        hold = (3*N) - r
        for i in range(N-1,-1, -1 ):
            if 1<=maps[i][hold]<=3:
                ans += (maps[i][hold]) ** 2
                team_no = tag_arr[i][hold] - 1
                team_haad = team_dir[team_no][3]
                ans += (tag_arr[hold][j][1] - team_haad) ** 2
                change_head(team_haad, team_no)
                return
        return
    
    else:
        hold = (4*N) - r
        for i in range(N):
            if 1<=maps[i][hold]<=3:
                ans += (maps[i][hold]) ** 2
                team_no = tag_arr[i][hold] - 1
                team_haad = team_dir[team_no][3]
                ans += (tag_arr[hold][j][1] - team_haad) ** 2
                change_head(team_haad, team_no)
                return
        return

def change_head(head_no, team_no):
    if head_no == 0:
        team_dir[team_no] = [0, len(team[team_no])-1, 1, 0]
    elif head_no != 0:
        team_dir[team_no] = [len(team[team_no])-1 , 0, (-1) , len(team[team_no])-1]
    return

print('이동전')
for m in tag_arr:
    print(m)

for i in range(30):
    # print(team)
    round_cnt += 1
    move()
    print('이동후')
    print('팀정보', team)
    for m in maps:
        print(m)
    ball()
print(ans)




