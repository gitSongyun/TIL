import sys

sys.stdin = open('sample_input.txt', 'r')
T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N: 문자열의 길이, K: K번째로 큰 수
    M = N // 4  # M: 한 변에 가능한 문자수
    nums = list(map(str, input()))  # nums를 받아옴
    nums += nums[0:M - 1]  # nums 앞에서부터 M개를 뒤에 덧붙여줌
    secret = [0] * N  # secret: 가능한 암호들을 담은 리스트
    len_s = N  # len_s: secret의 길이
    c = 0  # s: secret에 추가하기 위한 인덱스
    # 문자를 숫자로 변환하기 위한 딕셔너리
    change = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    # 비밀번호가 될 수 있는 조합 구하기
    for i in range(N):
        for n in range(i, N, M):
            add = nums[n:n + M]
            # 중복제거
            if add not in secret:
                secret[c] = add
                c += 1

    # 중복이 제거된 경우, 가능한 문자열만 남겨두고 제거
    while secret[-1] == 0:
        secret.pop()
        len_s -= 1

    # 진수로 표현된 문자를 정수로 변환
    for n in range(len_s):
        val = 0  # 초기값
        for m in range(M):

            # 문자가 숫자로변환 가능할 때, 10진수로 변환
            if secret[n][m].isdigit():
                val += int(secret[n][m]) * (16 ** (M - 1 - m))

            # A, B, C, D, E, F의 경우 딕셔너리를 이용해 숫자로 변환
            else:
                val += int(change[secret[n][m]]) * (16 ** (M - 1 - m))

        # 바꾼 값들을 원래 자리에 저장
        secret[n] = val

    # 정렬
    for n in range(len_s):
        for m in range(n, len_s):
            if secret[n] < secret[m]:
                secret[n], secret[m] = secret[m], secret[n]

    print(secret)
    # K 번째로 큰 수 출력
    # print('#{} {}'.format(tc, secret[K - 1]))