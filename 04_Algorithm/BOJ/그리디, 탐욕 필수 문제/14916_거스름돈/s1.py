import sys
sys.stdin = open('input.txt')

# 2, 5 짜리로만 거스름돈
N = int(input())

ans = 0

while True:
    if N%5 == 0:
        ans += N // 5
        break

    else:
        N-=2
        ans += 1

    if N<0:
        break
if N<0:
    ans = -1

print(ans)






