import sys
sys.stdin = open('input.txt')

total_sub, point = map(int, input().split())

total_mil = []

for i in range(total_sub):
    total_stu, can_stu = map(int, input().split())
    point_arr = list(map(int, input().split()))
    point_arr.sort()
    # print(i, total_stu)
    if total_stu < can_stu:
        total_mil.append(1)
    else:
        total_mil.append(point_arr[-can_stu])

# print(total_mil)
total_mil.sort()

# 하나씩 더하면서 point 보다 작을 때 까지 더한다
sum = 0
cnt = 0
for i in total_mil:
    # print(sum)
    sum += i
    cnt += 1
    if sum > point:
        sum -= i
        cnt -= 1
        break
# print(sum)
print(cnt)



