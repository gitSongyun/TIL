import sys
sys.stdin = open('input.txt')

answer = 0
todo_cnt = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(todo_cnt)]
# 정렬
schedule = sorted(schedule, key=lambda x : (x[0], x[1]))
# [(2, 4), (4, 5), (5, 6), (5, 7), (7, 9), (11, 12), (12, 12)]
print(schedule)
# 이어지는 날의 시작날짜와 끝 날짜 초기화
s, e = schedule[0]
duple_cnt = [0] * 366

for i in range(s, e+1):
    duple_cnt[i] = 1

maxx = 0
is_cont = False

# 날짜 확인
for i in range(1, todo_cnt):
    next_start, next_end = schedule[i]
    print(next_start, next_end)

    # 이어진다면
    if e + 1 >= next_start:
        print('이어진다')
        is_cont = True
        # 현재 끝나는 날짜가 이어진날짜의 끝나는 날짜 보다 작으면 갱신
        if e < next_end:
            e = next_end
        # 며칠이 젤 많은지 계산
        if next_start != next_end:
            for i in range(next_start, next_end+1):
                duple_cnt[i] += 1

        else: duple_cnt[next_start] += 1

    # 이어지지 않는다면, 현재까지 정보대로 코팅지 제작
    else:
        print('안이어진다, 계산하자')
        is_cont = False
        maxx = max(duple_cnt)
        answer += (e - s + 1) * maxx
        # 계산 후 초기화
        s, e = next_start, next_end
        # duple_cnt = [0] * 366
        for i in range(s, e + 1):
            duple_cnt[i] = 1
        maxx = 0

    print(f's={s}, e={e}, answer={answer}')
print('is_cont', is_cont)
print('duple_cnt', duple_cnt)

# 마지막 인덱스에선, 혼자남은 것인지, 이어진 날짜인지 구분,
if is_cont:
    answer += (e - s + 1) * max(duple_cnt)
else:
    answer += (e - s + 1) * 1


# 몇개가 이어 지는지 => 끝값 - 시작값 + 1


# 며칠이나 있는지, 각 일자를 카운트
print(answer)