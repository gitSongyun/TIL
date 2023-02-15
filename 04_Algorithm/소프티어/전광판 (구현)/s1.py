import sys

T = int(sys.stdin.readline())
# f는 자릿수 채움을 위한 가짜 0, 0은 실제로 켜진 0
code = {
    'f' : [],
    '0' : [1, 2, 3, 5, 6, 7],
    '1' : [3, 6],
    '2' : [1, 3, 4, 5, 7],
    '3' : [1, 3, 4, 6, 7],
    '4' : [2, 3, 4, 6],
    '5' : [1, 2, 4, 6, 7],
    '6' : [1, 2, 4, 5, 6, 7],
    '7' : [1, 2, 3, 6],
    '8' : [1, 2, 3, 4, 5, 6, 7],
    '9' : [1, 2, 3, 4, 6, 7]
}

# print(code[9])
for _ in range(T):
    be, af = map(str, sys.stdin.readline().split())
    if len(be) != len(af):
        be = be.rjust(5, 'f')
        af = af.rjust(5, 'f')

    answer = 0
    # 전광판 자릿수 하나씩 비교
    for i in range(len(be)):
        # 두 전광판의 켜진 전등을 합치고, 둘이 겹치는 전등을 뺀다면, after를 만들기 위해 뭐를 크고, 켜야 하는지 남게됨
        cnt = len((set(code[be[i]]) | set(code[af[i]])) - (set(code[be[i]]) & set(code[af[i]])))
        answer += cnt
    print(answer)

# 2 
# 1 
# 2 
# 9881 
# 10724