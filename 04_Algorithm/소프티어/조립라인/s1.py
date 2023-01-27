import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

line = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
a_work = 0
b_work = 0
a_line = 0
b_line = 0

for i in range(N - 1):
    # a에서 만 진행되는 경우,와 a에서 진행되다가 b로 넘어 가는 경우
    a_line = min(line[i][0] + a_work, line[i][1] + line[i][3] + b_work)
    # 그 반대
    b_line = min(line[i][1] + b_work, line[i][0] + line[i][2] + a_work)

    a_work = a_line
    b_work = b_line

result = min(a_line + line[N - 1][0], b_line + line[N - 1][1])

print(result)