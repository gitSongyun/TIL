# Gravity 풀이
# 2022-02-09

# 방의 크기
N=9

# 박스 갯수를 담을 list
box = list(map(int, input())) # [7,4,2,0,0,6,0,7,0]

# 낙차를 계산할 list
Falling= [0] * N


# 최대 낙차값은 맨 위에 놓인 박스가 된다. ex)7보다 높은 박스가 없다면 낙차값에 1을 더한다.
for i in range(0, N):
    for j in range(1+i, N):
        if box[i] > box[j]:
            Falling[i]+=1

        else:
            continue

# 최대 낙차값 찾기
max_val = Falling[0]
for i in Falling:
    if i >= max_val:
        max_val = i

print("최대 낙차는 : ", max_val)



