from collections import Counter

def solution(want, number, discount):
    answer = 0
    for i in range(0, len(discount) - 9):
        ten_dis = discount[i:i + 10]
        want_num = dict(zip(want, number))

        # 오늘의 할인 품목을 하나씩 넘겨 준다.
        for today_dis in ten_dis:
            if today_dis in want_num:

                want_num[today_dis] -= 1
                if want_num[today_dis] == 0:
                    want_num.pop(today_dis)

                if len(want_num) == 0:
                    answer += 1
                    break

            # 내가 원하는 항목이 없다면 내일로 미룬다.
            else:
                break

    return answer

# want = ["banana", "apple", "rice", "pork", "pot"]
# number = [3, 2, 2, 2, 1]
# discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]