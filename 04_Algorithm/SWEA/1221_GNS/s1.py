# 1221_GNS 풀이
# 2022-02-16
import sys
sys.stdin = open('GNS_test_input.txt', 'r')
T = int(input()) # 테스트 케이스 갯수

for t in range(1, T+1):
    a, tl = input().split() # a = 테스트 케이스 번호
    tl = int(tl) # tl = test case 길이

    # 순서대로 정렬하기 위한 리스트
    list_A = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    # 미정렬 리스트
    num_list = input().split()

    # 정렬 후 담을 리스트 생성
    ans_list = []

    # list_A의 원소들과 같은 값을 순서대로 뽑아내서 결과 리스트에 추가 한다.
    for i in list_A:
        for j in num_list:
            if i == j:
                ans_list.append(j)

    print("{}".format(a))
    for k in range(len(ans_list)):
        print(ans_list[k], end=" ")
    print()



