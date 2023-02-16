import sys
 
virus_num, p, time = map(int, input().split())
# 나머지 성질 이용
for _ in range(time):
    virus_num *= p
    # 안하면 시간초과가 남
    virus_num %= 1000000007
print(virus_num)

# 2 3 2