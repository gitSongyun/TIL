nums = [1, 3, -3, 2, 7, -4, 1, 8, 3, 9]

# 부분집합 구하기
for i in range(1 << 10):
    part = list()
    for j in range(10):
        if i & (1 << j):
            part.append(nums[j])
        sum_1 = 0

    # 모든 부분집합들의 합
    for p in part:
        sum_1 += p

    # 만약 합이 0이라면
    if sum_1 == 0:
        print(part)









