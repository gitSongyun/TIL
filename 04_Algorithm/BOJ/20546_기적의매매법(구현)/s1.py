import sys
sys.stdin = open('input.txt')


def junBuy(today):
    global jun_cash
    global jun_have
    if jun_cash // today > 0:
        jun_have += jun_cash // today
        jun_cash -= (jun_cash // today) * today

    return

def sungBuy(today):
    global sung_cash
    global sung_have
    global up_cnt
    global down_cnt
    global yesterday

    # 3일연속을 확인하기 위해 cnt 갱신
    if today > yesterday:
        up_cnt += 1
        down_cnt = 0
    elif today < yesterday:
        up_cnt = 0
        down_cnt += 1
    # print(today, up_cnt, down_cnt, sung_have, sung_cash)
    # 3일 연속 상승 시 전량 매도
    if up_cnt >= 3:
        # 매도 할 게 있다면
        if sung_have > 0:
            sung_cash += sung_have * today
            sung_have = 0
        

    # 3일 연속 하락 시  전량 매수
    if down_cnt >= 3:
        # 매수가 가능 하다면
        if sung_cash // today > 0:
            sung_have += sung_cash // today
            sung_cash -= (sung_cash // today) * today

    yesterday = today


jun_cash = sung_cash = int(input())
jun_have = sung_have = 0
up_cnt = down_cnt = 0
record = list(map(int, input().split()))
yesterday = record[0]

for today in record:
    junBuy(today)
    sungBuy(today)

# print(jun_have, jun_cash, sung_cash, sung_have)

jun_cash += jun_have * record[-1]
sung_cash += sung_have * record[-1]

# print(jun_cash, sung_cash)
if jun_cash > sung_cash: print('BNP')
elif sung_cash > jun_cash: print('TIMING')
else: print('SAMESAME') 
