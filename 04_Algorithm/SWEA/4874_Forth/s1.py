# 4874_Forth
# 2022-02-04

# 고려사항
# 연산자를 만났는데 stack 의 크기가 1 이하이면 error
# 나눗셈은 몫을 반환

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    arr = input().split()
    stack = []

    # 출력 기본값
    ans = 'error'
    for i in arr:

        # 마침표를 만나면 stack 에서 숫자를 pop 하여 출력하겠다.
        if i == '.':
            ans = stack.pop()
            break

        # 연산자를 만나면 arr 에서 두개를 pop 하여 연산 후 다시 넣는다.
        if i == '+' or i == '-' or i == '/' or i == '*':

            # 이때 stack 의 크기가 2 이상이 아니라면, 연산이 불가하므로 error
            if len(stack) < 2:
                ans = 'error'
                break

            elif i == '+':
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                stack.append(b+a)

            elif i == '-':
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                stack.append(b-a)

            elif i == '/':
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                # 나눗셈의 경우 항상 나누어 떨어지게 해야 하므로 몫을 push
                stack.append(b//a)

            elif i == '*':
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                stack.append(b*a)

        # 숫자면 stack 에 push
        else:
            stack.append(i)

    # 연산이 다 끝났는데도 stack 에 두 개 이상의 숫자가 남아 있다면 error 이다.
    if len(stack) > 2:
        ans = 'error'

    print("#{} {}" .format(tc, ans))
