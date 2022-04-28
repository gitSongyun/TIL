def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0]*MAXCANDIDATES
    if k == input:
        print(a)
        return
    else:
        k+=1
        # a에는 부분집합이 저장, k는 전체 원소의 갯수, c는 후보를 넣는 곳
        # 즉, c로 많은 숫자 중 0과 1만 후보로 쓰겠다는 의미
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            print('##',a)
            print(k)
            backtrack(a, k, input)     # [0, True, True, True] / k = 3 / input = 3
'''
## [0, True, 0, 0]
## [0, True, True, 0]
## [0, True, True, True]
## [0, True, True, False]

## [0, True, False, False]
## [0, True, False, True]
## [0, True, False, False]
## [0, False, False, False]

## [0, False, True, False]
## [0, False, True, True]
## [0, False, True, False]
## [0, False, False, False]
## [0, False, False, True]
## [0, False, False, False]
'''

def construct_candidates(a, k, input, c):
    c[0] = True  # 포함됨을 나타냄
    c[1] = False # 포함되지 않음을 나타냄
    return 2

MAXCANDIDATES = 2
NMAX = 4
a = [0]*NMAX
backtrack(a, 0, 3)
print('end')