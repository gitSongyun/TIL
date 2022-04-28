# 1234_비밀번호 풀이
# 2022-02-22
import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):

    N, arr = list(map(str, input().split())) # 글자의 갯수
    pw = []
    for i in arr:
        pw.append(int(i))

    idx = 0

    while idx < len(pw)-1:

        if pw[idx] == pw[idx+1]:
            pw.pop(idx)
            pw.pop(idx)

            if idx == 0:
                idx = 0

            else:
                idx -= 1

        else:
            idx += 1

    # print(pw)

    print("#{}" .format(tc), end=' ')
    for i in pw:
        print(i, end='')
    print()