import sys
sys.stdin = open('input.txt')

import re
p = re.compile('[A-F]?A+F+C+[A-F]?$')
N = int(input())
for _ in range(N):
    k = input()
    if p.fullmatch(k):
        print('Infected!')
    else:
        print('Good')




    # if set_STR[0] == "A" or set_STR[1] == "A":
    #     if




#  {A, B, C, D, E, F} 로 시작하거나 하지 않거나

# AFC가 연달아오고, 그뒤에거가 마지막에 없거나, ABCDEF 중 하나만 와야 한다.
# 즉 C로 끝나거나 혹은, 하나가 더있어야 하는데 그게 ABCDEF중 하나.
# 첫번째나 두번째가 A로시작하고,