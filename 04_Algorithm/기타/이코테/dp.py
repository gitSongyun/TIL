### 개미 전사
# 문제 : 개미는 두 칸간격으로 창고를 털 수 있다. 가장 최대로 털 수 있는 경우는?
# 창고 1개 이상을 털어야 한다. 
# storage = [1, 3, 1, 5]

# d = [0] * 100

# d[0] = storage[0]
# d[1] = max(storage[0], storage[1])

# for i in range(2, len(storage)):
#     d[i] = max(d[i-1], d[i-2] + storage[i])

# print(d)
# ---------------------------------------------------------------
### 1로 만들기 
x = 26
 
d = [0] * 30

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    print('현재값', i)
    if i%2==0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
    if i%5==0:
        d[i] = min(d[i], d[i//5]+1)
    print('d', d)

print(int('1101', 2))

