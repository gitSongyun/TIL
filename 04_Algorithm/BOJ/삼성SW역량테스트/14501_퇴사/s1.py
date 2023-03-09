import sys
sys.stdin = open('input.txt')

N = int(input())
table = [0 for _ in range(N)]
# dp 테이블
d = [0 for _ in range(N)]

# i일 만 존재할 때를 구하기 위해 
for i in range(N):
    time, pay = map(int, input().split())
    table[i] = [time, pay]
    d[i] = 0
    maxx = 0

    # 오늘 날짜 i + 소요시간 time을 더했을 때 N보다 작은 경우만 업무 가능
    if N < i + time:
        continue
    else :
        # 오늘 날짜 이전 값들 조회
        for j in range(0, i):
            # 만약 오늘 날짜 이전까지 완료한 일들중에 최대값 찾는다.
            if i >= j + table[j][0]:
                # 오늘 날짜 이전 j의 값은 누적값
                tmp = d[j]
                # 최대값 갱신
                if tmp > maxx:
                    maxx = tmp  
    # 오늘날짜 업무에 이전날짜 업무 최대값을 더하면, i일까지 일했을 때의 최대값을 얻을 수 있다.
    d[i] = pay + maxx

print(max(d))

     