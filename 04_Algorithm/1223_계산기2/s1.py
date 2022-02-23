# 1223_계산기
# 2022-02-23

import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = input()

    priority = {'+': 1, '*': 2}

    out = []
    stack = []
    for i in arr:
        # 연산자이면 스택에 push 한다.
        if i == '+' or i == '*':
            # 빈 스택이라면 일단 넣는다.

            if not stack:       # 전구 누르면 not으로 바뀜
                stack.append(i)
                continue        # 빈 리스트에 넣었으니 밑에 조건 다날리고 반복문 다시 돌아간다.

            # 우선순위 비교
            if priority[i] <= priority[stack[-1]]:   # 이 때 이전에 스택에 들어간 연산자와 우선순위 비교가 필요

                # 스택에 있는 연산자의 우선순위가 새로 들어갈 연산자의 우선순위보다 낮아지거나 빈 스택이 될 때 while 종료
                while stack != [] and priority[i] <= priority[stack[-1]]:
                    # 만약 새로 들어가는 놈이 같거나 더 낮다면 현재 있는게 나와야 하고
                    a = stack.pop(-1)
                    # 나온 연산자를 out에 넣는다.
                    out.append(a)

                # 다 끝나면 i를 stack에 넣는다.
                stack.append(i)

            # stack에 들어있는게 더 낮다면 그냥 들어간다.
            else:
                stack.append(i)

        # 숫자라면 out에 바로 넣는다.
        else:
            out.append(i)

    # 찌꺼기 연산자들을 뽑아낸다.
    while stack:
        out.append(stack.pop(-1))

    # 후위 표기법한 내용들을 연산할 두번째 스택
    stack_2 = []
    # 연산 내용을 담을 ans
    ans = 0

    # 반복문을 돌릴 땐, 내가 뭘 돌리고 있나 파악을 해야한다.
    for i in out:
        # 만약 연산자를 만나면 스택에서 두개 pop 후 연산하고 다시 stack에 넣는다.
        if i == '+':
            a = stack_2.pop(-1)
            b = stack_2.pop(-1)
            ans = int(b) + int(a)
            stack_2.append(ans)

        elif i == '*':
            a = stack_2.pop(-1)
            b = stack_2.pop(-1)
            ans = int(b) * int(a)
            stack_2.append(ans)

        # 숫자라면 out에서 pop한 값을 stack_2에 push 한다.
        else:
            stack_2.append(i)

    print("#{} {}".format(tc, stack_2[0]))
