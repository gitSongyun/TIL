def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0]*MAXCANDIDATES

    if k == input:
        for i in range(1, k+1):
            print(a[i], end= '')
        print()
    else:
        k+=1
        # 어떤 숫자들을 후보로 쓸지
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            print('##',a)
            print(k)
            backtrack(a, k, input)


def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k) :
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input+1):
        # 앞에서 사용되지 않은 애를 찾아서 후보에 추가
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1

    return ncandidates

MAXCANDIDATES = 2
NMAX = 4
a = [0]*NMAX
backtrack(a, 0, 3)
print('end')