import sys
sys.stdin = open('input.txt')

rock_cnt = int(sys.stdin.readline())
rock_height = list(map(int, sys.stdin.readline().split()))
answer = [1] * rock_cnt

for i in range(1, rock_cnt):
    max_ans = 0
    has_max = False
    # 첫 돌부터 현재 탐색중인 돌 전 까지, 작은돌을 찾고, 몇콤보 인지 찾은 후 거기에 +1을 한다.
    # 아마 다음에 보면 무슨말인지 모를것 같다.
    for j in range(0, i):
        if rock_height[j] < rock_height[i]:
            has_max = True
            if max_ans < answer[j]:
                max_ans = answer[j]

    if has_max:
        answer[i] = max_ans + 1
    else:
        answer[i] = 1

print(max(answer))