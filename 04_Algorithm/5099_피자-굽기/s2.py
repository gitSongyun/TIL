import sys

sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    data_i = [i for i in range(M)]
    data = list(map(int, input().split()))
    deq = []
    last = N-1
    while len(deq) < N:
        a = data_i.pop(0)
        deq.append(a)
        if len(data_i) == 0:
            break
    while len(deq) >= 1:
        idx_i = deq.pop(0)
        data[idx_i] = data[idx_i]//2
        if data[idx_i] == 0:
            last += 1
            if last >= M:
                continue
            deq.append(last)
        else:
            deq.append(idx_i)
    print("#%d %d"%(tc, idx_i+1))
# def FIRE(n, idx, ch):
#
#     # 화덕의 크기만큼 번호가 적힌 피자들을 넣는다.
#     for i in range(n):
#         queue.append(idx[i])
#
#     temp = []
#     k = 1
#     while queue:
#
#         # 화덕의 크기 만큼 반복문 돌린다.
#         for i in range(N):
#             if i == len(queue):
#                 break
#             # 이 때 자리를 한칸씩 밀어낸다.
#             temp = queue.pop(0)
#             queue.append(temp)
#
#
#             # 0번 인덱스(화덕입구)에 치즈가 0이 되는 피자가 왔을 때,
#             if ch[queue[0]] == 0:
#                 # 남은 피자가 있다면 그 자리에 새로운 피자를 넣는다.
#                 if n+k-1 < M: # n =3 k =1  => 3번 피자가 새로들어간다.
#                     queue[0] = idx[n+k-1]
#                     k += 1
#                 # 남은 피자가 없다면 화덕에서 그 피자를 뺀다.
#                 else:
#                     # print(queue, ch)
#                     queue.pop(0)
#                     # 피자를 뺐는데 화덕안에 피자가 한개 밖에 없다면 마지막 피자라는 의미
#                     if len(queue) == 1:
#                         # print(len(queue))
#                         # 마지막 피자의 번호를 출력한다.
#                         return print(queue[0]+1)
#
#         # 반복문이 다 돌면 화덕안 피자의 치즈를 2로 나누고 다시 돌린다.
#         for j in queue:
#             ch[j] = ch[j]//2
#         # print('queue:',queue)
#         # print('치즈상태',ch)
#
# for tc in range(1, T+1):
#     # N : 화덕의 크기, M : 피자의 갯수
#     N, M = list(map(int, input().split()))
#
#     # 피자들의 치즈 상태
#     ch = list(map(int, input().split()))
#     # 화덕의 역할
#     queue = []
#     # 번호가 적힌 피자들
#     idx = [i for i in range(M)]
#     FIRE(N, idx, ch)

# 테스트 케이스 출력
#1 4
#2 8
#3 6