# 1213_String 풀이
# 2022-Py-ch
import sys
sys.stdin = open('test_input.txt', 'r', encoding='utf-8')

for tc in range(1, 11):
    N = int(input()) # test case number
    p = input() # 검색할 문자열
    t = input() # 대상 문자열
    N = len(p)  # 검색할 문자열의 길이
    M = len(t)  # 대상 문자열의 길이

    cnt = 0

    # 대상 문자열을 검색 문자열의 길이만큼 잘라서 비교 해보겠다.
    for i in range(M-N+1):
        if t[i:i+N] == p:
            cnt += 1

    print("#{} {}".format(tc, cnt))

