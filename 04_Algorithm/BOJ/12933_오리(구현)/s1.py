import sys
sys.stdin = open('input.txt')
from collections import Counter
# [q, u, a, c, k]



match_str = 'quack'
cry = input()
match_idx = 0
cry_idx = 0

while True:

    #전체에서 인덱스 비교해간다.
    if cry[cry_idx] == match_str[match_idx]:
        cry_idx += 1
        if cry[cry_idx] == 'k':

    # q u a c k 순으로 찾는다.
    # 맞다면 해당 단어는 X 처리한다.
    # 만약 k인데, 그 뒤에 또 q라면 다시 match_str idx만 초기화하고 비교 (하나의 오리인지 확인)
    # 아니라면, 모두 초기화 하고 첨부터 다시 탐색


