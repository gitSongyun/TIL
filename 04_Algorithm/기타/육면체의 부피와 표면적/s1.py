# 문제 : 부피값 N 이상이 되면서, 표면적이 최소가 되기 위해 가로, 세로, 높이 를 최소한으로 하는 조건 찾기 
# 예시 : 가로 4, 세로 5, 높이 5 로 만들면 최소한의 표면적이 되면서 부피가 100이 된다. 
import math
N = 120 


# 대략적인 x,y,z 값 찾기
temp = math.trunc(N ** (1/3))
garo = [temp, temp, temp]

cnt = 2
while garo[0] * garo[1] * garo[2] >= N:
    
    garo[cnt % 3] += 1 

print(garo)
    


