# 5248_그룹 나누기
# 2022-04-05
import sys
sys.stdin = open('sample_input.txt')


def Find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[Find_set(y)] = Find_set(x)


T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))  # N: 학생수 , M: 신청서 수

    paper = list(map(int, input().split()))

    p = [i for i in range(N+1)]

    for j in range(0, len(paper), 2):
        union(paper[j], paper[j+1])


    print(p)
    ans = set()
    for k in range(1, N+1):
        ans.add(Find_set(k))
    print(ans)

    print('#{} {}'.format(tc, len(ans)))



