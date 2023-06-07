import sys
sys.stdin = open('input.txt')


# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))

u = [(0, False) for _ in range(n)]
d = [(0, False) for _ in range(n)]


def shift():
    temp = u[n - 1]
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[n - 1]

    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp


def can_go(idx):
    # 밖으로 나가는 것은 항상 가능합니다.
    if idx == n:
        return True

    # 안정성이 0보다 크면서 사람이 없는 경우에만
    # 이동이 가능합니다.
    stability, occupied = u[idx]
    return stability > 0 and not occupied


def move(idx):
    # 현재 위치에 있던 사람은 사라집니다.
    curr_stability, _ = u[idx]
    u[idx] = (curr_stability, False)

    # 밖으로 나가는 것이 아니라면,
    # 안정성이 1 감소하며, 사람이 추가됩니다.
    if idx + 1 < n:
        next_stability, _ = u[idx + 1]
        u[idx + 1] = (next_stability - 1, True)


def move_all():
    # 현재 위치에 사람이 있고, 그 다음 위치로 이동이
    # 가능한 경우에만 움직입니다.
    for i in range(n - 1, -1, -1):
        _, occupied = u[i]
        if occupied and can_go(i + 1):
            move(i)


def add():
    # 안정성이 0보다 크고 사람이 없는 경우에만
    # 첫 번째 위치에 사람을 올려놓습니다.
    stability, occupied = u[0]
    if stability > 0 and not occupied:
        u[0] = (stability - 1, True)


def simulate():
    # Step1. 무빙워크를 한 칸 회전시킵니다.
    shift()

    # Step2. 사람들을 한 칸씩 앞으로 이동시킵니다.
    move_all()

    # Step3. 사람을 새로 올립니다.
    add()

    # Step4. n번 칸 위치에 사람이 있다면, 즉시 내려줍니다.
    _, occupied = u[n - 1]
    if occupied:
        move(n - 1)


def done():
    unstable_cnt = 0
    for stability, _ in u:
        if not stability:
            unstable_cnt += 1

    for stability, _ in d:
        if not stability:
            unstable_cnt += 1

    return unstable_cnt >= k


given_row = list(map(int, input().split()))
for i, stability in enumerate(given_row[:n]):
    u[i] = (stability, False)
for i, stability in enumerate(given_row[n:]):
    d[i] = (stability, False)

trial = 0

while not done():
    simulate()
    trial += 1


print(trial)