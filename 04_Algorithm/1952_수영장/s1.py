# 1952_수영장
# 2022-03-27

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))         # 가격
    plan = [0] + list(map(int, input().split()))    # 계획
    expense = [0 for _ in range(13)]                # 누적합

    for i in range(1, 13):
        # 우선 1일권을 끊었을 때와 1달권을 끊었을 때 어느 것이 더 작은지 구분한다.
        day = om = 0 # 1일권 끊었을 때 경우, 한달 끊었을 때 경우
        day = plan[i] * price[0]
        om = price[1]

        expense[i] = min(day, om) + expense[i-1] # 둘 중 적은 비용을 찾고, 저번달 비용에 더하면 누적 합이 된다.

        # 그 다음 3달권을 끊었을 때와 비교한다.
        # 3달권은 3월 이후로 비교가 가능하다. 0 10 20 30
        if i > 2:
            expense[i] = min(expense[i], price[2]+expense[i-3])  # 3달권 가격+3달전 누적합, 3달치 누적 합을 비교해 더 작은 값을 갱신한다.
        print(expense)
        ans = min(expense[12], price[3])

    print("#{} {}".format(tc, ans))














