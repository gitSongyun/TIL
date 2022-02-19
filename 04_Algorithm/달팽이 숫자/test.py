arr_1 = [4,5,2,3,1]


for a in range(4):
    minIdx = a
    for b in range(a + 1, 5):
        if arr_1[minIdx] > arr_1[b]:
            minIdx = b
    arr_1[a], arr_1[minIdx] = arr_1[minIdx], arr_1[a]
    print(arr_1)

#2번 반복문 시작 :  4
# [1, 2, 5, 4, 3]
# [1, 3, 5, 4, 2]

#for i in range(25):
