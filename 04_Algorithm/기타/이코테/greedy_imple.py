"""
이코테 그리디, 구현 문제
"""
### 1이 될 때 까지
# N = 3
# # 나눌 수 있는 수
# K = 4
# cnt = 0
# while True:
#     if N < K:
#         break
#     # K 로 나눠지는 수가 새로운 타겟이 된다.
#     target = (N//K) * K
#     # N-target = target이 될 때 까지 1을 몇번 빼야 하는지 알 수 있다. 
#     cnt += (N - target)

#     cnt += 1
#     N //= K
# cnt += (N - 1)
# print(cnt)
# --------------------------------------------------------------------------------
### 곱하기 혹은 더하기 
# S = '567'
# answer = 0
# for s in S:
#     s = int(s)
    
#     if answer == 0 or s<=1:
#         print('1이하', s)
#         answer += s
#     else:
#         print('2이상', s)
#         answer *= s

# print(answer)
# --------------------------------------------------------------------------------
### 모험가 길드
# N = 5
# arr = [2, 3, 1, 2, 2]

# arr.sort()
# temp =[]
# answer = 0
# for i in arr:
#     temp.append(i)

#     if len(temp) >= i:
#         answer += 1
#         temp = []
#     else:
#         continue
# print(answer)
# --------------------------------------------------------------------------------
### 상하좌우 : 여행가 위치
# # 배열크기
# N = 5
# # 이동방향
# Move = "RRRUDD"
# # 맵 생성
# arr = [[0] * N for _ in range(N)]

# position = [0, 0]
# command = {
#     'R' : [0, 1],
#     'L' : [0, -1],
#     'U' : [-1, 0],
#     'D' : [1, 0]
# }

# for m in Move:
#     print(m)
#     x, y = command[m]
#     print(x,y)
#     nx = position[0] + x  
#     ny = position[1] + y
#     if nx < 0 or nx > N or ny < 0 or ny > N:
#         continue
#     else:
#         position[0] = nx
#         position[1] = ny
    
# position[0] += 1
# position[1] += 1
# print(position)
# --------------------------------------------------------------------------------
### 왕실 나이트
# input = ['c', '2']

# x, y = input
# y = ord(x) - 97
# x = int(y) - 1
# print(x,y)

# dx = [-2, -2, -1, 1, 2, 2, 1, -1]
# dy = [-1, 1, 2, 2, 1, -1, -2, -2]
# answer = 0
# for i in range(8):
#     nx = x + dx[i]
#     ny= y + dy[i]

#     if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
#         print(nx, ny)
#         answer += 1
# print(answer)
# --------------------------------------------------------------------------------
### 문자의 재정렬
S = 'K1KA5CB7'

answer = ''

str_arr = ''
int_arr = 0

for s in S:
    
    if s.isdigit():
        int_arr += int(s)
    else:
        str_arr += s
str_arr = ''.join(sorted(str_arr, key=lambda x:x))

print(str_arr+str(int_arr))
         