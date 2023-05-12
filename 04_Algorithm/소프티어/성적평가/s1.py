import sys

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] > high_arr[h]:  # 내림차순이므로 부등호 방향 변경
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

N = int(sys.stdin.readline())
result = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
game = -1
# 3번 반복
total_res = [0 for _ in range(N)]
game = -1
game_rank = [{}, {}, {}]
for res in result:
    sort_res = sorted(res, reverse=True)
    person = -1
    game += 1
    for rank, score in enumerate(sort_res):
        if score in game_rank[game]:
            continue
        game_rank[game][score] = rank + 1
    for r in res:
        person += 1
        print(game_rank[game][r], end=' ')
        total_res[person] += r
    print()

s_res = sorted(total_res, reverse=True)
res = {}
for idx, val in enumerate(s_res):
    if val in res:
        continue
    res[val] = idx + 1

for tot in total_res:
    print(res[tot], end=' ')