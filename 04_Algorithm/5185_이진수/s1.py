# 5185_이진수
# 2022-03-24
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    N, arr = list(input().split()) # 16진수 갯수

    hexa = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}


    # 전체 이진수를 담을 문자열
    ans = ''

    for i in arr:
        # 만약 알파벳 이라면 그에 대응하는 정수로 변환
        if i in hexa:
            num = hexa[i]
            x = hexa[i]

        # 숫자라면 int로 변환
        else:
            num = int(i)
            x = int(i)

        # 이진수 변환
        binary = ''
        while num!= 0:
            binary = str(num % 2) + binary
            num = num //2

        # 변환된 이진수의 길이가 4가 되도록 0을 채워준다.
        while len(binary) < 4:
            binary = '0'+binary

        # 결과를 차례대로 붙여준다.
        ans += binary
    print("#{} {}".format(tc, ans))



