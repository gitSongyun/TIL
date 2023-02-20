import sys
sys.stdin = open('input.txt')

p = input()
n = int(input())
def solution(p, n):
    # am pm 부분 슬라이싱
    am_pm = p[:2]

    hour_sec = 60 * 60
    min_sec = 60

    hour = n // hour_sec
    if hour >= 25:
        hour = hour % 24
    remainder = n % hour_sec
    minute = remainder // min_sec
    sec = remainder % min_sec

    # '시분초' 슬라이싱
    hour_slice = p[3:5]
    min_slice = p[6:8]
    sec_slice = p[9:]

    new_sec = int(sec_slice) + sec
    new_min = int(min_slice) + minute
    new_hour = int(hour_slice) + hour

    if new_sec >= 60:
        new_min += 1
        new_sec -= 60
    if new_min >= 60:
        new_hour += 1
        new_min -= 60

    if am_pm == 'PM':
        new_hour += 12
    new_hour %= 24

    new_hour = str(new_hour).zfill(2)
    new_min = str(new_min).zfill(2)
    new_sec = str(new_sec).zfill(2)

    answer = new_hour + ':' + new_min + ':' + new_sec
    return answer

print(solution(p, n))
