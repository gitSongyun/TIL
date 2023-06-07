import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
rail = list(map(int, input().split()))

rail_num = 2*N                          # 레일 갯수
rail_idx = [i for i in range(rail_num)] # 회전을 표시할 리스트
people = []
zero_cnt = 0
ans = 0
safe = True

# 1. 회전
def rotate():
    for j in range(rail_num):
        rail_idx[j] = (rail_idx[j] -1 + rail_num) % rail_num

    # 회전 후 N번 레일에 온사람 내리게 함, 뒤에서부터 탐색
    for i in range(len(people)-1, -1, -1):
        if people[i] == -1:
            break
        # 회전했는데 N번 레일에 왔다면 내려야 한다.
        if rail_idx[N - 1] == people[i]:
            people[i] = -1

    return

# 2. 앞으로 이동
def move():
    global zero_cnt

    # 맨 처음 탄 사람부터 이동해야 하므로 0부터 시작
    for i in range(len(people)):
        is_there = False
        if people[i] == -1:
            continue
        next = (people[i] + 1 + rail_num) % rail_num

        # 다음 레일의 안정성이 0이상이고
        if (rail[next] > 0):
            for j in range(len(people)-1, -1, -1):
                if people[j] == -1 :
                    continue

                # 사람이 없는 칸이라면
                if i != j and people[j] == next:
                    is_there = True
                    break
            # 누가 있으니까 다음 사람 탐색
            if is_there:
                continue

            # 이동
            people[i] = next
            # 이동 후 레일 안정도 -1
            rail[next] -= 1
            # 만약 그 레일이 N번째 레일이라면, 내리게 한다.
            if rail_idx[N - 1] == next:
                people[i] = -1
            # 이동 후 안정성 체크
            if rail[next] == 0:
                zero_cnt += 1
            # print(people, '이동후')
    return

# 2. 태우기
# 탈 때 마다 people에 추가 하기
def onRail():
    global zero_cnt
    first = rail_idx[0]
    if rail[first] > 0:
        people.append(first)
        rail[first] -= 1
         # 태우고 안정성 체크
        if rail[first] == 0:
            zero_cnt += 1
    return

# 안정성이 0인 개 몇개인지 체크 할 함수
def isSafe():
    global safe
    cnt = 0
    for i in range(len(rail)):
        if rail[i] == 0:
            cnt += 1
    # print(cnt, K)
    return cnt < K

while isSafe():          # N 번 반복
    ans += 1
    rotate()
    move()

    onRail()


print(ans)
