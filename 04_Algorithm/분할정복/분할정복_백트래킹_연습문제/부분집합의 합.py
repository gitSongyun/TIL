# 부분집합의 합이 10이 되는 부분집합을 구하라

def DFS(L,P,s):
    global cnt
    cnt += 1

    # 부분집합의 합이 10이 넘어가면 return 한다.
    if sum(P) > 10:
        return

    if s == 10:
        if sum(P) == 10:
            print(P)
    else:
        DFS(L,P,s+1)
        DFS(L,P+[L[s]],s+1)

L = [1,2,3,4,5,6,7,8,9,15]
cnt = 0
DFS(L,[],0)
print(cnt)