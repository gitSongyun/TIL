ip = '0269FAC9A0'

decode = {'001101': 0, '010011': 1, '111011': 2, '110001': 3,
          '100011': 4, '110111': 5, '001011': 6, '111101': 7,
          '011001': 8, '101111': 9
          }

hexa = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

ans = ''

for i in ip:
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
    while num != 0:
        binary = str(num % 2) + binary
        num = num // 2

    # 변환된 이진수의 길이가 4가 되도록 0을 채워준다.
    while len(binary) < 4:
        binary = '0' + binary

    # 결과를 차례대로 붙여준다.
    ans += binary

result = ''
j = 0
i = 0
while i < len(ans)//6:

    a = ans[j+6*i: j+6+6*i]

    if len(a) < 6:
        break

    print(ans[j+7*i: j+6+7*i], i, j)
    if a in decode:
        result += str(decode[a])
        i += 1

    else:
        j += 1
print(result)


