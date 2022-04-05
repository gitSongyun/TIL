# 1206_View 풀이
# 2022-02-19
import sys
sys.stdin = open('input.txt', 'r')
T = 10

for tc in range(1, T+1):

    num = int(input()) #건물의 갯수
    apt = list(map(int,input().split())) # 건물들 층수


    # 맨 앞 두칸은 건물이 없으므로 현재 위치는 2부터
    current = 2
    result = 0
    while current < num-2 : # 양쪽 두 칸은 건물 없음 2 ~ 97

        # 현재 위치 건물 기준으로 양쪽 2칸씩 슬라이싱
        temp = apt[current-2:current+3] # [0, 0, 225, 214, 82]
        # print(temp)

        # 가장 높은 아파트 확보
        max_apt = 0
        for j in range(1, 5):
            if max_apt < temp[j]:
                max_apt = temp[j]
        j = 0

        # 만약 현재위치 건물이 제일 높은 건물이라면
        # if temp[2] == max_apt and temp[0] != temp[2] and temp[1] != temp[2] and temp[3]!=temp[2] and temp[4]!=temp[2]:
        if temp[2] == max_apt:
            current += 3 # 오른쪽 두칸은 확정적으로 조망권 없으므로 3칸 이동후 탐색
            # 조망권 확보 숫자는 높이 차이가 가장 작은 숫자가 된다.
            min_gap = 255 # 아파트 최대 높이가 255 이므로
            for i in range(0,5):
                gap = max_apt - temp[j]
                if 0 < gap and min_gap > gap:
                     min_gap = gap
                     print(min_gap)
            result += min_gap
            
        # 탐색중인 건물이 제일 높은 건물이 아니라면 그 다음 아파트를 기준으로 탐색한다.
        else:
            current += 1




    print(result)







