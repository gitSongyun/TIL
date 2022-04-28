def f(i, N, K): # i 부분집합에 포함 될 지 결정할 원소의 인덱스, N, 전체 원소 갯수
    if i == N: # 한개의 부분집합 완성
        # print(bit, end= ' ')
        s = 0
        for j in range(N):
            if bit[j]:
                s += a[j]
            #     print(a[j], end = ' ')
            # print()
        if s == K: # 찾는 합이면
            for j in range(N):
                if bit[j]:
                    print(a[j], end=' ')
            print()
    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i+1, N, K)
    return
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(a)
bit = [0] * N
f(0, N, 10) # 합이 10인경우를 찾아봐