import sys
sys.stdin = open('input.txt')

k = int(input())
tangerine = input()

def solution(k, tangerine):
    answer = 0

    # 크기별 갯수를 담을 list
    cnt_tan = {}

    # 크기별 갯수를 담는다.
    for tan in tangerine:
        if tan in cnt_tan:
            cnt_tan[tan] += 1
        else:
            cnt_tan[tan] = 1

            # 제일 갯수가 많은 크기대로 정렬
    cnt_tan = dict(sorted(cnt_tan.items(), key=lambda x: x[1], reverse=True))

    for j in cnt_tan:
        k -= cnt_tan[j]
        answer += 1
        if k <= 0:
            return answer

    return answer

print(solution(k,tangerine))
