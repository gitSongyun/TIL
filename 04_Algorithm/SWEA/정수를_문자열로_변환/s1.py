ㅈ#정수를_문자열로_변환
#2022-02-16

x = int(input())

# 정수를 각각 담을 리스트
num_bfo = []

# 문자열로 변환한 내용을 담을 리스트
num_aft = []

# 정수를 한 자리수 씩 각각담는다.
while x != 0:
    num_bfo.append(x%10)
    x = x // 10

# 거꾸로 들어갔기 때문에 반전 시킨다.
num_bfo = num_bfo[::-1]

# 각 숫자에 48을 더해주면 그 숫자과 동일한 문자가 출력된다.
for i in range(len(num_bfo)):
    num_aft.append(chr(num_bfo[i]+48))
    print(num_aft[i], end='')
