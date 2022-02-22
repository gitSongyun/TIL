import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 배열의 길이, M : 구간합의 길이
    N, M = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    R = N - M + 1 # 10-3+1 = 8번, 10개 배열에는 3개의 구간합을 8개 만들 수 있다.

    sum_a = [0] * R

    for i in range(R): # 9
        for j in range(M): # 3
            sum_a[i] += arr[i+j] # 구간합을 차곡차곡 담았다.

            # 이제 최대,최소값을 
            for z in range(M):


    print(sum_a)
