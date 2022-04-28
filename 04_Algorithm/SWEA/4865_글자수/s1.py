# 4865_글자수
# 2022-02-17

import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # 테스트 케이스 갯수

for tc in range(1, T+1):
    dict = {'str1' : input(), 'str2' : input()}

    max_cnt = 0

    # 반복문으로 str1과 str2를 하나씩 비교해서 같다면 cnt를 올린다.
    for i in (dict['str1']):
        # 비교문자가 바뀌면 cnt를 초기화 한다.
        cnt = 0
        for j in (dict['str2']):
            # str1의 글자와 str2의 글자가 일치하면 cnt에 +1을 한다.
            if i == j:
                cnt += 1

        # cnt가 max_cnt 보다 크다면 새롭게 갱신한다.
        if max_cnt < cnt:
            max_cnt = cnt


    print("#{} {}".format(tc, max_cnt))
