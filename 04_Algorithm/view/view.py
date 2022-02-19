# view 풀이
# 2022-02-10


import sys
sys.stdin=open("input.txt")

T = 10 # Testcase=10

apt_cnt = int(input())
height = map(int, input())


# for i in range(2, T): # 맨앞,뒤 두칸은 건물이 없으므로 2부터
