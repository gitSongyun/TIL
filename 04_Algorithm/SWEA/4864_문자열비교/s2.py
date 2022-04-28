# 4864_문자열비교
# 2022-02-17

import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for t in range(1, T+1):

    str1 = list(input()) # 찾고싶은 문자열
    str2 = list(input()) # 대상 문자열

    cnt = 0
    i = j = 0
    cnt = 0

    # str1 또는 str2의 탐색이 끝나면 반복문은 종료된다.
    while i < len(str1) and j < len(str2) :

        # 만약 문자가 같다면, i와 j를 다음 인덱스로 넘기고 cnt + 1을 한다.
        if str1[i] == str2[j]:
            i += 1
            j += 1
            cnt += 1

        # 만약 다르다면 i 는 초기화
        # j는 str1과 str2가 같기 시작한 부분의 다음 idx로 가야 한다.
        # ex) AABB
        #     AAABB 
        else:
            i = 0
            j = j - cnt + 1
            cnt = 0

    # str1의 길이와 cnt가 같다면 str2에 str1이 존재한다는 의미
    if cnt == len(str1):
        print("#{} 1" .format(t))
    else:
        print("#{} 0" .format(t))

# 잘못한 점
# while 조건을 잘 못 설정했다...