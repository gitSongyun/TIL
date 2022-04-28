# 부분집합의 합이 0이되는 집합들 찾아내기

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)

result = []
for i in range(0, (1<<n)):
    sum = 0
    ans = []
    for j in range(0, n):

        if i & (1 << j):
            sum += int(arr[j])
            ans.append(str(arr[j]))
    if sum == 0:
        result.append(ans)

for i in result:
    print(i)



