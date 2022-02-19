import random

# 1~26 숫자가 랜덤으로 정렬된 테스트 케이스 생성
num_list = []
for a in range(1,26):
    num_list.append(a)
random.shuffle(num_list)

# 2차원 리스트로 만들 리스트 생성
N=M=5
temp= [[0]*N for _ in range(M)]

# 2차원 리스트로 만들 반복문
cnt=0
for i in range(5):
    for j in range(5):
      temp[i][j]=num_list[cnt]
      cnt+=1

print(temp)

# 우 하 좌 상 순으로 인접한 요소를 뽑을 장치
dk = [0, 1, 0, -1]
dl = [1, 0, -1, 0]

sum_1=0

# 5X5 행렬에서 인접한 4개의 요소를 뽑겠다.
for k in range(5):
    for l in range(5):
        for m in range(4):
            nk = k + dk[m] # 행
            nl = l + dl[m] # 열

            # 인덱스가 4를 넘어선 안되기 때문에 조건문 생성
            if 0<=nk<N and 0<=nl<M:
                # 둘의 차이를 절대값으로 뽑기 위한 조건문
                if temp[nk][nl] < temp[k][l]:
                    sum_1 += temp[k][l]-temp[nk][nl]
                else:
                    sum_1 += temp[nk][nl] - temp[k][l]
print(sum_1)