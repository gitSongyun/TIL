import sys
sys.stdin = open('input.txt')

N, X = map(int, input().split())
num_arr = list(map(int, input().split()))
win_sum = 0
maxx_sum = 0
maxx_cnt = 0

for i in range(N):
    win_sum += num_arr[i]
    if i >= X-1:
        if maxx_sum == win_sum:
            maxx_cnt += 1
            

        if maxx_sum < win_sum:
            maxx_sum = win_sum
            maxx_cnt = 1
        win_sum -= num_arr[i-(X-1)]

if maxx_sum == 0:
    print('SAD')
else:
    print(maxx_sum)
    print(maxx_cnt)
# print(maxx_sum, maxx_cnt)