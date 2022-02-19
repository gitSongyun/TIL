# 4828_숫자카드 풀이
# 2022-02-10


import sys
sys.stdin=open("sample_input.txt")

T = int(input())


for i in range(0,T):
    # 카드의 번호를 idx와 대응시키고 갯수를 넣기 위한 list 생성
    card_cnt = [0] * 10
    N = int(input()) # 카드의 총 갯수
    a_i = list(map(int,input())) # 뽑은 카드 list

    # 같은 숫자의 카드가 몇 개 있는지 계산. 9번 카드가 2개라면 card_cnt[9] = 2
    for j in a_i:
        card_cnt[j]+=1

    # 갯수가 가장 많은 카드의 넘버와 갯수 계산
    max_val = 0
    for k in range(len(card_cnt)): # k는 카드 넘버,
        # k번 카드의 갯수가 max 갯수보다 크다면
        if card_cnt[k] >= max_val:
            # card_num은 k번 이 되고,
            card_num = k
            # k번 카드의 갯수를 max_val에 넣는다.
            max_val = card_cnt[k]

    print("#{} {} {}".format(i+1, card_num, max_val))


