# 보물상자 비밀번호

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    N, K = list(map(int,input().split())) # N: 문자갯수, K: 몇 번째로 큰 수를 뽑을 건지
    arr = list(input())

    dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    # 사각형 한 변에 몇개의 문자가 있는지
    end = N//4

    # 슬라이스 한 내용들을 넣을 list
    set_list = []

    rotate = 0
    # 로테이션 시키면서 slice 하기
    while rotate < end:

        # 한 변의 문자들을 슬라이싱
        for i in range(0, N, end):
            set_list.append(arr[i:end+i])

        # 로테이션을 하면 한 자리씩 밀린다.
        temp = [0]*N # 자리를 한 칸씩 밀린 원소들을 잠시 담을 리스트
        for j in range(N-1):
            temp[j + 1] = arr[j]
        temp[0] = arr[-1]
        arr = temp
        rotate += 1

    # 16진수 -> 10진수 한 내용들을 result 에 넣는다.
    result = []
    for i in set_list:
        ans = 0
        for j in range(end):

            # A~F 의 문자가 나오면 dict 의 value 를 이용해 다음과 같이 계산
            if i[j] == 'A' or i[j] == 'B' or i[j] == 'C' or i[j] == 'D' or i[j] == 'E' or i[j] == 'F':
                ans += dict[i[j]] * (16**(end-1-j))

            # 숫자가 나온 경우
            else:
                ans += int(i[j]) * (16**(end-1-j))

        # 10진수로 변환한 값을 result 에 넣음
        result.append(ans)

    # 중복된 것을 없애기 위한 set
    s1 = set(result)
    # 다시 list 로 변환
    s1 = list(s1)

    # 내림차순 정렬
    for i in range(len(s1)-1):
        for j in range(len(s1)-1):
            if s1[j] < s1[j+1]:
                s1[j], s1[j+1] = s1[j+1] ,s1[j]

    print("#{} {}".format(tc, s1[K-1]))



