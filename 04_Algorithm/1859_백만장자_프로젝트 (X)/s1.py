# 1859_백만장자 프로젝트
# 2022-02-20

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 거래 일

    arr = list(map(int,input().split()))

    # 리스트에서 최대값을 찾고 그 최대값
 