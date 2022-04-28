# Gravity 풀이
# 2022-02-09


N = 9 # 눕혔을 때 높이

# 박스 갯수를 담을 list
box = list(map(int, input()))  # 8보다 작은 수를 입력해야 함, [7,4,2,0,0,6,0,7,0]

# 낙차를 계산할 list
Falling = [0] * 8


for i in range(1, N): # 쌓아올린 갯수 1~8
    cnt = 0
    for j in range(0, N): # 박스 idx 0~8
        if i > box[j]: # 0개인 칸이 몇 개 인가
            cnt += 1
            Falling[j] = cnt

print(Falling)
# max_val = Falling[0]
# for i in Falling:
#     if i >= max_val:
#         max_val = i
#
# print("최대 낙차는 : ", max_val)



