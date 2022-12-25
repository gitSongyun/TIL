    # import sys
# sys.stdin = open('input.txt')

# T = 10

# for tc in range(1, T+1):

#     N = int(input()) # N = 길이
#     s = input()      # N

#     icp = {'(': 3, '*': 2, '+': 1}
#     isp = {'(': 0, '*': 2, '+': 1}

#     tokens = []
#     stack = []
#     result = []

#     # 괄호를 만나면 tokens 에 넣고, 숫자는 stack에 넣는다.
#     for i in range(N):

#         # 숫자면 result 추가한다.
#         if s[i].isdigit():
#             result.append(s[i])

#         # 괄호면 tokens 에 추가한다.
#         elif s[i] == '(':
#             tokens.append(s[i])

#         # 닫히는 괄호를 만나면 열리는 괄호를 만날 때 까지 stack 을 pop 한다.
#         elif s[i] == ')':
#             while tokens[i] != '(':
#                 result.append(tokens.pop(-1))

#         # 연산자면 우선순위를 비교 한 후에 알맞게 넣는다.
#         else:
#             # 들어가는 것보다 안에 있는게 더 작다면 pop 한다.
#             while icp[s[i]] < tokens[-1]:
#                 tokens.pop(-1)



v = [1,3]

a = [1,2]
print(v +a)
